#  [Bavarian Cristus](https://bcristus.herokuapp.com/)

[Click here to visit the site.](https://bcristus.herokuapp.com)

Bavarian Cristus is a website created by Luciano Fernández with the purpouse of allowing all people interested in Jesus Christ, that also enjoy to take and share photos, and happen to be residents or visiting Bavaria, to share their pictures and thoughts about images shared by others.

Users of the website are able to see images and also upload their own taken photos to a Jesus statue, as long as they are taken within Bavaria.

They will be also able to tag the location of the photo. This will allow visitors to find exactly where the statue is located.


AQUI VA FOTO DE LAS CAPTURAS DE PANTALLA DEL MEDIDOR DE RESPONSIVIDAD
Image	![alt text](image.jpg)

In the home page, visitors can watch a list of post; each card appears to be a traditional PostCard. !! Among others, an expected update of this website will be allowing to create a PDF file from those post card; to be shared or even sent per post upon request.

AQUI VA FOTO DE UNA DE LAS POSTALES, AGREGALE UN SIMBOLO DE EXPORTAR PDF
Image	![alt text](image.jpg)

The post card contains an image and information about the author of the picture; !! those fields as well as messages could be printed or not upon request of the member using checkboxes. Members of the community can also comment and like other posts.

In this version, each post have a location tag to locate the statue. !! in future releases, the user will be able to tag the exact location, this is with the purpouse of making routes for tourists and groups of visitors and guided tours.

Footer; in the footer there's access to social network and the traditional rights reservation statement.

The website is written within github development enviroment, using Django as MVC (MVT) framework and deployed to Heroku. All images and static files are being hosted in Cloudinary.

## Working Methodology

In order to achieve this first release, i set up tasks having in mind an Agile mindset and stablishing goals to be completed within weekly iterations.

Placing myself in the user's position, and anticipating the user's wants and needs, i made myself the following questions:

Why would a user want to visit our blog?
What will make them return
What do i want to see when I visit a blog
What would make me return

From those answer I did set up 17 issues in GitHub as User Stories.

### User Stories

- EPICS
    - User Storys

- I can see photos posted by other users on this particular topic with no hassel.
    - As a user, I can see photos posted by other users so that i get interest on becoming a member.
    - As a user, I can see comments on each photo post so that i get interest on becoming a member.
        
- To be part of a community.
    - As a user, i can easily log in using email and social media profiles, so that i become a member.
    - As a member, I can publish my own taken photos so that users can see them.
    - As a member, I can writte comments so that i can share opinions on this images.
    - As a member, I can like/unlike photos so that i can share opinions on this images.
    - As a member, I can like/unlike comments so that i can share opinions on this images.
    - As a member, I can tag a point in the Map with location of the statue so that others can plan a visit.
    - As a member, I can see how many people looked/liked the post so that i get interest in keep posting.
    - As a member, I can have a profile with a gallery of my own taken images so that i can store and share in other social media platforms.
    - As a member, I can share images so that i share in other social media platforms.

- Discover the places those photos were taken on and planning trips.
    - As a user, I can see a tag in the map where the photo was taken, so that i can plan a visit.

- Managing and mantainig the website
    - As an Admin I can create post so that they can be showed in the website
    - As an Admin, I can Approve/Deny photos before posting so that i can review contents quality.
    - As an Admin, I can post members photos to our own Social media so that they have more visibility.


AQUI VA FOTO DE UNA DE LAS USER STORIES DE GITHUB
Image	![alt text](image.jpg)

Which then i organized using Moscow prioritazion.

AQUI VA FOTO DE UNA DE LAS ETIQUETAS DE STORIES DE GITHUB
Image	![alt text](image.jpg)

## Database Design
    
### Models

I will be using three diferent database models for this project: User, ImagePost and Comments,

The User class is the default User class from Django.

The ImagePost class is the key custom class in this project as the main function of the site is for users to share their own taken images, both inherit from models.Model.


class ImagePost(models.Model):

    title = models.CharField(max_length=200, unique=False)
    slug = models.SlugField(max_length=200, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_images')
    author = models.CharField(max_length=255)
    image = CloudinaryField('image')
    location = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    excerpt = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='image_likes', blank=True)



class Comment(models.Model):

    text = models.TextField()
    image_post = models.ForeignKey(ImagePost, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments_made')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)


### Database Relationships

I found is necessary to have two foreign keys in the Comment model to establish a relationship between the Comment model, the ImagePost model, and the User model.

The image_post foreign key in the Comment model is used to associate each comment with an specific image post. This creates a one-to-many relationship between the ImagePost model and the Comment model, as each ImagePost can have multiple Comment instances associated with it.

The user foreign key in the Comment model is used to track the user who made the comment. This creates a one-to-many relationship between the User model and the Comment model, as each User can have multiple Comment instances associated with it.



UPDATEUPDATEUPDATEUPDATEUPDATEUPDATE 

<img src="media/readme/EDR-Bavarian-Cristus.png">


## Users Types.

There's three type of expected users.
1. Visitors:
    - Will be able to watch all posts.
    - Find the statue in a map within the post (beta).
    - Will be able to register as a member using a valid email.

2. Members
    Including visitors access, member Will be able to:
    - Create Posts
    - Edit and delete their own posts.
    - Make comments on other members posts.
    - Like posts.
    - Share images in their social network from within our site (beta).

3. Admin
    Including members access, Admin is able to:
    - Aprove or deny posts.
    - Delete or banned users.

## CRUD Capabilities

All members have the hability to:
- Create posts, to be showed upon approval.
- View their own posts. 
- Update and edit their own post.





- Introduction
- Working Metodology
    - User Stories
    - Moscow Prioritization
- Database Design
    - Database Relationships
    - Models
- Users types
- CRUD Capabilities


Comment CRUD Stories
Like Stories
Feedback Stories
UI Stories
Search and Filter Stories

- Agile Workflow
Adding essential features first.
GitHub Features
    Issues
    Projects
- Features
Admin Panel
allauth authentication
Home Page

Favorites
My Books
Add a Book
Delete a Book
Modify a Book Entry
Leaving a Comment
Liking a Book
Alerts
Filter and Search
Filter by User
Filter by Genre
Search by Author, Title, Description
No Results Found
404
- Testing
Code Validation
Behavior Driven Development (BDD)
Version Control Strategy
- Unfixed Bugs
Features to Improve
- Deployment
Technology used
Project Creation
Deployment to Heroku
- Credits
Page Image Credits
Book Genre Image Credits