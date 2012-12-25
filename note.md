#Django_model
model表关系，一张表里边的两个外键组成的关系是多对多

#Django confusing me
##Spanning multi-valued relationships

	>>> d = Blog.objects.filter(entry__headline__contains="beat", entry__pub_date__year=2012)
	>>> d 
	[<Blog: shi blog>, <Blog: dean blog>]
	>>> d = Blog.objects.filter(entry__headline__contains="beat").filter(entry__pub_date__year=2012)
	>>> d
	[<Blog: shi blog>, <Blog: shi blog>, <Blog: dean blog>, <Blog: dean blog>, <Blog: dean blog>]

##Lookups that span relationships  blog ---> entry  one ---> many

	>>> e = Entry.objects.filter(bolg__name="dean blog")
	>>> e
	[<Entry: lennonn>, <Entry: deanshishang>, <Entry: shangbeatal>]
	>>> b = Blog.objects.filter(entry__headline="lang")
	>>> b
	[<Blog: shi blog>, <Blog: shang blog>]
	>>> b = Blog.objects.get(pk=1)
	>>> b.entry_set.all()
	[<Entry: lennonn>, <Entry: deanshi>, <Entry: shangbetale>]
	>>> b.entry_set.count()
	3

