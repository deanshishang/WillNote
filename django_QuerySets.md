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

###Complex lookups with Q objects

###Comparing objects

###Delete objects

###Copying model instances

###Undating multiple objects at once

###Related objects
####One-to-many relationships
####Many-to-many relationships
####One-to-one relationships


##QuerySet method reference

