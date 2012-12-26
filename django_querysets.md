#QuerySets

##Executing queries
Once you have created your data models, Django automatically give you a database-abstraction API that let you create, retrieve(检索), update and delete objects.

###Create objects 

	from blog.models import Blog
	b = Blog(name="XXXX", taglines="XXXX")
	b.save() #do not forget
	INSERT SQL statement

To create and save an object in a single step, use the create() method.

###Saving changes to objects

	b.name = "XXXX"
	b.save()
	UPDATE SQL statement

####Saving ForeignKey and ManyToManyField fields

	from blog.models import Entry
	entry = Entry.objects.get(pk=1)
	cheese_blog = Blog.objects.get(name="Cheddar Talk")
	entry.blog = cheese_blog
	entry.save()

	from blog.models import Author
	joe = Author.objects.create(name="Joe")
	entry.authors.add(joe)

	baul = Author.objects.create(name="Baul")
	george = Author.objects.create(name="George")
	entry.authors.add(baul, george)

###Retrieving objects
To construct a QuerySet via a Manager on your model class.*NOTE:*SELECT statement
You get a QuerySet by using your model's Manager, Each  model has at least one Manager, and it's called objects by default, Access it directly via the model calss.
Managers are accessible only via model classes, rather than from model instances, to enforce a separation between "table-level" and "record-level"

####Retrieving all objects

	all_entries = Entry.objects.all()

####Retrieving specific objects with filters

	filter(**kwargs)
	exclude(**kwargs)

The lookup parameters(**kwargs)should be in the format described in Filde lookups below.

	Entry.objects.filter(pub_date__year=2006)

You only need all() when you want all objects from the root QuerySet

	Chaining filters
	Entry.objects.filter(headline__startwith="What").exclude(pub_date__gte=datetime.now()).filter(pub_date__gte=datetime(2005,1,1))

####Retrieving a single object with get

	one_entry = Entry.objects.get(pk=1)
	
if there is no Entry object with a primary key of 1, Django will raise Entry.DoesNotExist (MultipleObjectsReturned)

####Other QuerySet methods
####Limiting QuerySets
	Entry.objects.all()[:5]
	Entry.objects.all()[5:10] #[-1]is not supported
	Entry.objects.all()[:10:2] #every second object of the first 10
	
	Entry.objects.order_by('headline')[0]
	SELECT foo FROM bar LIMIT 1
	Entry.objects.order_by('headline')[0:1].get()
	*NOTE:*however, that the first of these will raise an IndexError while the second will raise DoesNotExist if no objects match the given criteria.

####Field lookups
	field__lookuptype=value
	Entry.objects.filter(pub_date__lte='2006.02.13')
	SELECT * FROM blog_entry WHERE pub_date <= '2006-02-13'

	Entry.objects.filter(blog_id__exact=4)

	Entry.objects.get(headline_exact="Man bites dog")
	SELECT ... WHERE headline = 'Man bites dog'
	
If you do not provide a look up type, the lookup type is assumed to be exact
	
	Blog.objects.get(id__exact=4)
	Blog.objects.get(id=4)
	The above two are equivalent

	iexact A case-insensitive match
	contains / icontains
	Entry.objects.get(headline__contains='Lennon')
	SELECT ... WHERE headline LIKE "%Lennon%"

	startswith / endswith
	istartswith / iendswith

####Lookups that span relationships
This example retrieves all Entry objects with a Blog whose name is 'Beatles Blog'
	
	Entry.objects.filter(blog__name__exact='Beatles Blog')

This spaning can be as deep as you'd like
It works backwards,too.
	
This example retrieves all Blog objects which have at least one Entry whose headline contians 'Lennon'

	Blog.objects.filter(entry__headline__contains='Lennon')

If you are filtering across multiple relationships and one of the intermediate models does not have a value that meets the filter condition,Django will treat it as if there is an empty(all values are NULL), but valid.

	Blog.objects.filter(entry__authors__name='Lennon')

If there was no author associated with an entry, it would be also treat as if there was also no name attached, rather than raising an error because of the missing author.

	Blog.objects.filter(entry__authors__name__isnull=True)
	Blog.objects.filter(entry__authors__isnull=False, entry__authors__name__isnull=True)

#####Spanning multi-valued relationships

	>>> d = Blog.objects.filter(entry__headline__contains="beat", entry__pub_date__year=2012)
	>>> d
	[<Blog: shi blog>, <Blog: dean blog>]
	>>> d = Blog.objects.filter(entry__headline__contains="beat").filter(entry__pub_date__year=2012)
	>>> d
	[<Blog: shi blog>, <Blog: shi blog>, <Blog: dean blog>, <Blog: dean blog>, <Blog: dean blog>]

####Filters can reference fields on the model (过滤器可以在模型上引用字段) F() expression
What if you want compare the value of a model field with another field on the same models?

	from django.db.models import F
	Entry.objects.filter(n_comments__gt=F('n_pingbacks'))
	Entry.objects.filter(n_comments__gt=F('n_pingbacks')*2)
	Entry.objects.filter(authors__name=F('blog)__name'))

For date and date/time fields you can add or subtract a timedelta object. The following would return all entries that were modified more than 3 days after they were published

	from datetime import timedelta
	Entry.objects.filter(mod_date__gt=F('pub_date')+timedelta(days=3))

####The pk lookup shortcut

	Blog.objects.get(id__exact=14)
	Blog.objects.get(id=14)
	Blog.objects.get(pk=14)

####Escaping percent signs and underscores in LIKE statements ---> automatically escape

	Entry.objects.filter(headline__contains='%')
	SELECT ... WHERE headline LIKE '%\%%'

####Caching and QuerySets
Each queryset contains a cache, to minimize database access, It is important to kown how it works,in order to write the most efficient code.

	print [e.headline for e in Entry.objects.all()]
	print [e.pub_date for e in Entry.objects.all()]
	re-use!
	query = Entry.objects.all()
	print [p.headline for p in query]
	print [p.pub_date for p in query]

###Complex lookups with Q objects
If you need to excute more complex queris like OR statement, you can use Q objects.
Q objects can be combined using the & and | operators. When an operator is used on two Q objects, it uields a new Q object.

	from django.db.models import Q
	Q(question__startwith="Who") | Q(question__startwith='What')
	WHERE question LIKE 'Who%' OR question LIKE 'What%'

	Q(question__startwith='Who') | ~Q(pub_date__year=2005)

	Poll.objects.get(Q(question_startwith="Who"), Q(pub_date=date(2005, 5, 2))|Q(pub_date=date(2005, 5, 6)))
	SELECT * from polls WHERE question LIKE 'Who%' AND (pub_date='2005-05-02' OR pub_date='2005-05-06')
If a Q object is provided, it must precede the defination of any keyword arguments.
	VSALID QUERY ---> equivalent to the previous example.
	Poll.objects.get(Q(pub_date=date(2005, 5, 2))|Q(pub_date=date(2005, 5, 6)), question__startwith='who')
	INVALID QUERY--->
	Poll.objects.get(question__startwith='Who',Q(pub_date=date(2005, 5, 2))|Q(pub_date=date(2005, 5, 6)))
	
###Comparing objects
The following two statements are equivalent:
	
	some_entry == other_entry
	some_entry.id == other_entry.id # compare primary key values og two models.

Comprisons will always use the primary key, whatever it's called

###Delete objects
	
	e.delete()

This deletes all Entry objects with a pub_date year of 2005.

	Entry.objects.filter(pub_date__year=2005).delete()

This will delete the Blog and all of its Entry objects

	b = Blog.objects.get(pk=1)
	b.delete()

delete() is the only QuerySet method that is not exposed on a Manager itself. This is a safety mechnism to prevent you from accidentally requesting Entry.objects.delete(), and delete all the entries. If you do want to delete all the objects, then you have to explicitly request a complete query set.

	Entry.objects.all().delete()

###Copying model instances
No built-in method for copying model instance, but it is possible to easily create new instance with all field;s valuee copied. You can just set pk to None.

	blog = Blog(name="My blog", tagline='Blogging is easy')
	blog.save()  #post.pk == 1
	blog.pk = None
	blog.save() #post.pk == 2

Things get more complicated if you use inheritancce. Consider this

	class ThemeBlog(Blog):
		theme = models.CharField(max_length=200)

	django_blog = ThemeBlog(name="XXX", tagline='XXX', theme='python')
	django_blog.save() # django_blog.pk == 3

Due to how inheritance works, you have to set both pk and id to None

	django_blog.pk = None
	django_blog.id = None
	django_blog.save() #django_blgo.pk == 4

This process does not copy related objects, If you want to copy relations, you have ti write a little bit more code. Entry has a many to many field to Author

	entry = Entry.objects.all()[0] #some previous entry
	old_authors = entry.authors.all()  #???
	entry.pk = None
	entry.save()
	entry.authors = old_authors #saves new many2many relations

###Undating multiple objects at once
Sometimes you want to set a filed to a paricular value for all the objects in a QuerySet. You can do this with the update() method.
	
	Entry.objects.filter(pub_date__year=2007).update(headline='Everythings')

To update a non-relation filed, provide the new value as a constant, To update ForeignKey fields, set the new value to be the new model instance you want to point to

	b = Blog.objects.get(pk=1)
	Entry.objects.all().update(blog=b)
		
You can filter based on related fields, but you can only unpdate columns inthe model's main table.

	b = Blog.objects.get(pk=1)
	#update all the headlines belonging to this Blog.
	Entry.objects.select_related().filter(blog=b).update(headline = 'thins')

Be aware that update method is covered directly to an SQL statement.It is a bulk operation for direct updates.(批量操作直接更新),If you want to make sure that the save() special function to handle that, just loop over them and call save()

	for item in my_queryset:
		item.save()

Calls update can also use F() objects to update on field based on the value of another field in the model.This is especially useful for incrementing counters based upon their current value.

	Entry.objects.all().update(n_pingbacks=F('n_pingbacks')+1)

You can not introduce joins when you use F() objects in an updated, if that, a filederror will be raised.
	
	#raise error
	Entry.objects.update(headline=F('blog__name'))

###Related objects
When you define a relationship in a model, instance of that model will have a convenient API to access the related object(s).

An Entry object e can get its associated Blog object by accessing the blog attribute

	e.blog
*NOTE:*Behind the scenes, this functionality is implemented by python descriptors.(通过python描述符来实现)

Django also creates API accessors for the 'other' side of the relationship -- the link from related model to the model that defines the relationship
	
	b.entry_set.all()

####One-to-many relationships
#####Forward
		
	e = Entry.objects.get(id=2)
	e.blog

	
	e = Entry.objects.get(id=2)
	e.blog = some_blog
	e.save()

If a ForeignKey field has null=True set(it allows NULL values), you can assign None to it.

	e = Entry.objects.get(id=2)
	e.blog = None
	e.save()
	
Forward access to one-to-many relationships is cached the first time the related object is accessed. Subsequent accesses to the foreign key on the same object instance are cached

	e = Entry.objects.get(id=2)
	print e.blog #hits the database to retrieve the associated blog
	print e.blog #does not hits the database use cached version

Note that the selected() queryset method recursively prepolulates the cache of all one-to-many relationships ahead of time.

	e = Entry.objects.get(id=2)
	print e.blog #does not hits the database, use cached version
	print e.blog #does not hits the database use cached version

#####Backward

	b = Blog.objects.get(id=1)
	b.entry_set.all() #returns all entry objects related to blog

	#b.entry_set is a Manager that returns QuerySets
	b.entry_set.filter(headline__contains='ddd')
	b.entry_set.count()

You can override the FOO_set name by setting the related_name parameter in the ForeignKey() definition

	blog = ForeignKey(Blog, related_name='entries')
	b.entries.all()
	b.entries.count()

You can not access a reverse ForeignKey Manager from the class, it must be accessed from an instance

	Blog.entry_set
	Traceback:
	....Manager must be accessed via instance

Other method

	add(obj1, obj2, ...)
	create(**kwargs)
	remove(obj1, obj2, ...)
	clear() #removes all objects from the related object set.

If the clear() method is not available, all objects in the iterable will be added without removing any exitsing dlements

	b.entry_set = [e1, e2]

Each reverse operation described in this section has an immediate effect on the database. Every addition, creation and deletion is immediately and automatically saved to the database.

####Many-to-many relationships
Both ends of a many-to-many relationship get automatic API access to the other end, The API works just as a "backward" one-to-many relationship,above.

The only difference is in the attribute nameing: The model that defines the ManaToManyField uses the attribute name of that field itself.

	e = Entry.objects.get(id=3)
	e.authors.all()
	e.authors.filter(name__contains='Jhon')

	a = Author.objcets.get(id=2)
	a.entry_set.all()  #also can specify related_name.

####One-to-one relationships
It is very similar to many-to-one relationships, instances of that model will have access to the related object via a simple attribute of the model

	class EntryDetail(models.Model):
		entry = models.OneToOneField(Entry)
		details = models.TextField()

	ed = EntryDetail.objects.get(id=2)
	ed.entry #returns the related Entry object

That Manager represents a single object, rather than a collection of objects

	e = Entry.objects.get(id=1)
	e.entrydetail #return the related EntryDetail object if no, raise a DoesNotExist exception

Instance can be assigned to the reverse relationship in the same way as you would assign the forward relationship

	e.entrydetail = ed

How are the backward relationships possible?
Other object-relational mappers require you to define relationships on both sides. The django developers believe this is a violationi(违反) of the DRY principle, so Django only requires you to define the relationshipe on the end.

But how is this possible, given that a model class does not know which other model classes are releted to it until those other model classes are loaded?

The answer lies in the INSTALLD_APPS settings. The first time any model is loaded, Django iterates over every model in INSTALLED_APPS and creates the backward relationships in memory as needed.

####Queries over related objects
Following three queries would be identical:
	
	Entry.objects.filter(blog=b)
	Entry.objects.filter(blog=b.id)
	Entry.objects.filter(blog=5)

###Falling back to raw SQL
[Performing raw SQL queries](https://docs.djangoproject.com/en/1.4/topics/db/sql/)

##[QuerySet method reference](https://docs.djangoproject.com/en/1.4/ref/models/querysets/)

