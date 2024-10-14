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


## Users Types

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

All members have the ability to:
- Create posts, to be showed upon approval.
- View their own posts. 
- Update and edit their own post.
- Delete their own post.

All this abilities were tested successfully.

## Features

### Design and Colors

- Navigation fonts tend to be sober and respectful; text style contrast with solid background colors.
- Cinzel Decorative and Roboto, Imported from google fonts are the fonts to be used.
- Color selection is intended to remember colors at church and in general catholic styles.
- Colors used in this website are:
    - RGBA(245, 221, 7, 0.86)
    - RGBA: (173, 135, 98, 1)
    - RGBA: (250, 235, 215, 1)
    - RGBA(195, 155, 114, 0.71)

<img src="readme/colors.png">


### Navigation

- Featured at the top of the page, the navigation shows the website's name in the left corner BAVARIAN CRISTUS, which is to be showed in every page and links to the home page.

<img src="readme/navbar.png">


The menu collapses in a sandwich icon from medium media queries, and the navigation elements get underlined when displayed.


<img src="readme/navbarreduced.png">
<img src="readme/navbarreduced2.png">

### Home Page

The home page is designed to show a list with each post rendered as a Traditional Post Card; which contains fields to show information about the post. However features for writting a message from the card and export as PDF were hidden because are not functional yet.

In order to access the post, we must click either the image or the title of the post; clicking the name under "Posted By:" must take us to the profile from the member who upload the image.


<img src="readme/PostCard.png">

### Post Details

Once Inside the post, we will look at the image in full size, with a frame according to the website colors.

Below the image, we sill see the Post title and the likes functionallity; together with the number of comments written for this post.

We can see too the name of the post's author. Here the posts can be created, edited or deleted. 

All comments that have been made for this post can be viewd here as well; if the user is authenticated will be able to post a message himself, will be only showed upon approval though. 


<img src="readme/postdetail.png">


By clicking the "Create" button, members can create new posts.


<img src="readme/create.png">


By clicking the "Edit" button, members can edit their post's Title, Location, Description Text and replace the uploaded image; they can also make a post not publish.


<img src="readme/edit.png">


By clicking the "Delete" button, members can delete their post, the button leads to a confirmation page for this action.

<img src="readme/confirmdelete.png">

At the bottom of the post page commes a map, the members will have the opportunity to tag the location where they took the photo. Is not properly connected yet.

### Profile page

By clicking in the Member name, he will access his profile page, where he can find a button to upload new post, and all content that was already uploaded.


<img src="readme/Profile.png">

### About page

The "about" link, brings the users to a static template with a brief explanation of the website's purpose (to be extended).

<img src="readme/about.png">


## Manual Testing





### CRUD

- I ran manual tests to create a new User.

1. Click "Register" button at the left-top corner.

<img src="readme/register1.png">


2. Fill fields for Username, email (not required), Password and confirmation.
    - Password Cannot be similar than username.

    <img src="readme/register2.png">


3. User is Successfully Created.
    - Can See username and logged in icon.
    - Can Click icon  at the top-left corner to Logout

    <img src="readme/register3.png">

Once the user was created, 

- I ran manual tests to create a post.

1. Click on the username and inside the page, click the "Create new Post" button.

<img src="readme/create1.png">


2. Complete all fields and upload an image, i did update an image intended to be replaced.


<img src="readme/create2.png">


3. The post shows succesfully in the user's profile.


<img src="readme/create3.png">


Once the post was created, 

-   I ran manual test to Edit a Post.

1. Click on the post's title in order to enter the Post Details page, Once inside, click on the "Edit" button.

<img src="readme/edit1.png">


2. Modify the fields to be updated.


<img src="readme/edit2.png">


3. Both Image and text content were updated succesfuly.


<img src="readme/edit3.png">

Once the post was edited, 

-   I ran manual test to Delete a Post.

1. Click on the title of the post we want to delete.


<img src="readme/delete1.png">


2. Click on the "Delete" Button


<img src="readme/delete2.png">


3. Will redirect to a confirmation page; we must confirm and the post will be deleted.


<img src="readme/delete3.png">


4. Will then redirect to the User's profile with no post to show.


<img src="readme/delete4.png">







I ran test manually for verify CRUD functionallity for loading posts.






- In the top-right corner, users can find the website menu; with three links redirecting to "Home", "Gallery' and "Post" pages respectively, each one has a diferent page.










- Introduction
- Working Metodology
    - User Stories
    - Moscow Prioritization
- Database Design
    - Database Relationships
    - Models
- Users types
- CRUD Capabilities
- Features
    - Design and Colors
    - Navigation
        - Home Page
        - Post Detail
        - Profile page
        - About
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