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

##Copying model instances

	entry = Entry.objects.all()[0] #some previous entry
	old_authors = entry.authors.all()  #???
	entry.pk = None
	entry.save()
	entry.authors = old_authors #saves new many2many relations

#Interesting directories and contents
## /
The root directory where the file system begins, In most cases the directory only contains subdirectories

## /boot
This is where the linux kernel and boot loader files are kept. The kernel is a file called vmlinuz

## /etc
The /etc directory contains the configuration files of system. All file in this directory should be text files
### /etc/passwd 
It contains essential information for each user. It is here that users are defined.
### /etc/fstab
It contains a table of device that get mounted when you system boots, defines your disk driver
### /etc/hosts
This file list the network host names and IP addresses that are intrinsically(本质上) known to the system
### /etc/init.d
This directory contains the script that statr various system services typically at boot time

## /bin, /usr/bin
These two directories contain most of the programs for the system. /bin directory has the essential programs that the system requires to operate, while /usr/bin contains applications for the system users

## /sbin /usr/sbin
For system administration. Mostly for use by the superuser.

## /usr
It contains a varity of thins that support user applications.
### /usr/share/X11
support fules for the X window system
### /usr/share/dict
Dictionary for the spelling checker. 
### /usr/share/doc
Various documentation files in a variety of formats
### /usr/share/man
man page here
### /usr/src
Source code file, if you installed the kernel code package, you will find the entire linux kernel sourcecode here

## /usr/local
Used for the installation of software and other file for use on the local machine. What this really means is that software that is part of the official distribution goes here.
When you find interesting programs to install on your system, they should be installed in one of the /usr/local directories. Most often, the directory of choice is/usr/local/bin.

## /var
The /var directory contains files that change as the system is running.This includes:
### /var/log
Directory that contains log files. These are updated as the system runs. You should view the files in this directory from time to time, to monitor the health of your system.
### /var/spool
This directory is used to hold files that are queued for some process, such as mail messages and print jobs. When a user's mail first arrives on the local system (assuming you have local mail), the messages are first stored in/var/spool/mail

## /lib
The shared libraries(similar to DLLs in that other operating system) are kept here

## /home
Where users keep their personal work.This keeps things nice and clean

## /root
Superuser's home directory

## /tmp
It is a directory in which programs can write their temporary files

## /dev
The /dev directory is a special directory, since it does not really contain files in the usual sense. Rather, it contains devices that are available to the system. In Linux (like Unix), devices are treated like files. You can read and write devices as though they were files. For example /dev/fd0 is the first floppy disk drive, /dev/sda (/dev/hda on older systems) is the first hard drive. All the devices that the kernel understands are represented here.

## /proc
The /proc directory is also special. This directory does not contain files. In fact, this directory does not really exist at all. It is entirely virtual. The /proc directory contains little peep holes into the kernel itself. There are a group of numbered entries in this directory that correspond to all the processes running on the system. In addition, there are a number of named entries that permit access to the current configuration of the system. Many of these entries can be viewed. Try viewing /proc/cpuinfo. This entry will tell you what the kernel thinks of your CPU.

## /media /mnt
hich is used in a special way. The/media directory is used for mount points. As we learned in the second lesson, the different physical storage devices (like hard disk drives) are attached to the file system tree in various places. This process of attaching a device to the tree is called mounting. For a device to be available, it must first be mounted.When your system boots, it reads a list of mounting instructions in the file /etc/fstab, which describes which device is mounted at which mount point in the directory tree. This takes care of the hard drives, but you may also have devices that are considered temporary, such as CD-ROMs, thumb drives, and floppy disks. Since these are removable, they do not stay mounted all the time. The /media directory is used by the automatic device mounting mechanisms found in modern desktop oriented Linux distributions. On systems that require manual mounting of removable devices, the /mntdirectory provides a convenient place for mounting these temporary devices. You will often see the directories /mnt/floppy and /mnt/cdrom. To see what devices and mount points are used, type mount.


