from basic import db,Puppy

## Create ##

mypuppy = Puppy('Rufus',5)
db.session.add(mypuppy)
db.session.commit()

## READ ##
all_puppies = Puppy.query.all()
print(all_puppies)

#select by ID
puppy_one = Puppy.query.get(1)
print(puppy_one.name)

#Filters
#by name
puppy_frankie = Puppy.query.filter_by(name='Frankie')
print(puppy_frankie.all())

#Update
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()

##Delete
# second_puppy = Puppy.query.get(2)
# db.session.delete(second_puppy)
# db.session.commit()

#
all_puppies= Puppy.query.all()
print(all_puppies)