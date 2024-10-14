# [Bavarian Cristus](https://bcristus.herokuapp.com/) v2

[Click here to visit the site.](https://bcristus.herokuapp.com)

[Click here to visit repository.](https://github.com/EL1909/bavarian-cristus-PP4.git)

<img src="readme/CoverBC.jpg">

---

- [Introduction](#bavarian-cristus)
- [Assessment Results](#assessment-results)
- [Working Methodology](#working-methodology)
    - [User Stories](#user-stories)
    - [Moscow Prioritization](#moscow-prioritization)
- [Database Design](#database-design)
    - [Database Relationships](#database-relationships)
    - [Models](#models)
- [Users Types](#users-types)
- [CRUD Capabilities](#crud-capabilities)
- [Features](#features)
    - [Design and Colors](#design-and-colors)
    - [Navigation](#navigation)
        - [Home Page](#Home_Page)
        - [Post Detail](#Post_Detail)
        - [Profile page](#profile-page)
        - [About](#about-page)
        - [Likes](#likes)
- [Testing](#manual-testing)
    - [Manual Testing](#manual-testing)
        - [CRUD](#crud)
        - [Messages](#messages)
    - [Automated Testing](#automated-testing)
    - [CSS Validator](#css-validator)
    - [LightHouse](#lighthouse)
- [Project Creation Process](#project-creation-process)
- [Deployment to Heroku](#deploy-to-heroku)
- [Bugs](#bugs)
    - [Unfixed](#unfixed)
    - [Fixed](#fixed)
- [Features to Improve](#features-to-improve)
- [Credits](#credits)

---


Bavarian Cristus is a website created by Luciano Fernández with the purpouse of allowing all people interested in Jesus Christ, that also enjoy to take and share photos, and happen to be residents or visiting Bavaria, to share their pictures and thoughts about images shared by others.

Users of the website are able to see images and also upload their own taken photos to a Jesus statue, as long as they are taken within Bavaria.

They will be also able to tag the location of the photo. This will allow visitors to find exactly where the statue is located.

In the home page, visitors can watch a list of post; each card appears to be a traditional PostCard. Among others, an expected update of this website will be allowing to create a PDF file from those post card; to be shared or even sent per post upon request.

<img src="readme/PostCard.png">

The post card contains an image and information about the author of the picture; those fields as well as messages could be printed or not upon request of the member using checkboxes. Members of the community can also comment and like other posts.

In this version, each post have a location tag to locate the statue. In future releases, the user will be able to tag the exact location, this is with the purpouse of making routes for tourists and groups of visitors and guided tours.

In the footer there's access to social network and the traditional rights reservation statement.

The website is written within github development enviroment, using Django as MVC (MVT) framework and deployed to Heroku. All images and static files are being hosted in Cloudinary.

## Assessment Results

This is the second version i make of this website, the following list contains notes from assessor and steps taken to deliver a solution.

- All text needs to have a positive font color contrast ratio.
    - Modified color scheme on text areas.
- Favicon should be included for the website.
    - Added favicon.ico to root directory.
- The website is responsive but users need to be allowed to store and manipulate data records about a particular domain.
    - Responsiveness improved.
- Ensure that all user stories have a descriptive user acceptance criteria.
    - To be implemented in future projects.
- Error pages should be implemented.
    - Error pages are implemented.
- Clicking on like on a post results in a not found error.
    - Links are verified.
- Additionally all attempts to create a post resulted in a not found error when the post was clicked on.
    - This error was caused due a permission configuration, now post can be published without admin's approval.
- The CRUD logic for users to create, locate, display, edit and delete records is present, but not fully implemented to work as expected.
    - Whole CRUD operation was reviewed and fixed for publishing posts.
- Implement form validation and verification so that users cannot submit blank or incorrectly filled forms. 
    - Form validation implemented in text field and location when post are created.
- All attempts to create a post resulted in a not found error when the post was clicked on.
    - This error was caused due a permission configuration, now post can be published without admin's approval.
- The testing process needs to be documented in a little more detail to explain all the manual and automated tests undertaken including the testing steps, results and outcomes of each test and this should also include user story testing.
    - Whole CRUD operation was reviewed and fixed for publishing posts.
- The website needs to provide options for effective user actions, with relevant feedback for all user actions.
    - Whole CRUD operation was reviewed and fixed for publishing posts.


## Working Methodology

In order to achieve this second release, i review tasks and repair most of the mistakes that lead to a failure in the first place.

There's still more features to be implemented, having in mind an Agile mindset and stablishing goals to be completed within weekly iterations.

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


<img src="readme/userstory.png">


## Moscow Prioritization
Which then i organized using Moscow prioritazion.

<img src="readme/moscow.png">

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


<img src="readme/EDR-Bavarian-Cristus.png">


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
- Create posts.
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


<img src="readme/navtop.png">


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

## Making a Post

1. In the main page, user are able to Sign in, or SignUp for a new Account.

<img src="readme/SignIn.jpg">

2. Once logged in, User can access it's profile by clicking his name on the top bar or in the PostCard name in the home Page

<img src="readme/Accessprofile.png">

3. By clicking the "Create new Post" button, members can create new posts.


<img src="readme/create01.png">

4. User must:
    1. Writte a title for the image. 
    2. Select an image to upload.
    3. Introduce a location where the image was taken, there's form validation in this field to include the word "Bayern" as all images in the website must be from within Bayern.
    4. User Must writte a brief review on the picture, There's form validation to ha at least 6 characters in the description.

<img src="readme/create.png">

5. If all fields are filled correctly,
user will be sent to it's profile page, where can see the new post.

<img src="readme/create02.png">

6. By clicking the image, or the title, we can access the image Post page

<img src="readme/postimage.png">

7. By clicking the "Edit" button, members can edit their post's Title, Location, Description Text and replace the uploaded image; they can also make a post not publish.


<img src="readme/edit.png">


8. By clicking the "Delete" button, members can delete their post, the button leads to a confirmation page for this action.


<img src="readme/confirmdelete.png">


At the bottom of the post page commes a map, the members will have the opportunity to tag the location where they took the photo. Is not properly connected yet.


### Profile page

By clicking in the Member name, he will access his profile page, where he can find a button to upload new post, and all content that was already uploaded.


<img src="readme/Profile.png">

### About page

The "about" link, brings the users to a static template with a brief explanation of the website's purpose (to be extended).

<img src="readme/about.png">

### Likes

Inside the Post detail, there is an icon for the user to like the post. If the user has already liked the post, the icon is filled. Otherwise it is empty. The total likes are displayed next to the icon. When the user clicks on the like icon, the status toggles - like goes to unlike and vice versa.


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


With this tests i verified my CRUD operations to be working successfully for creating posts.

### Messages

I ran test manually to verify message functionallity.

1. Visiting the site without registration, messages functionallity is hidden.


<img src="readme/messages1.png">


2. From within a members account, the "Leave a Message:" field appears, Writte the message and submit.


<img src="readme/messages2.png">


3. The member is notified that this comment requires to be approved ny admin.
 

<img src="readme/messages3.png">


4. Once the comment is approvd by the Admin, will show in the post detail page.


<img src="readme/messages4.png">


## Automated Testing

I did wrote three automates test following the Django Blog walkthru project, however i didn't had time to actually run them.

## CSS Validator
Css validator showed no errors.

## Lighthouse

## Project Creation Process

I created this project following both "Django Blog" and the "I Think Therefore I Blog projects".

I followed the stepst as Follows:

### In Gitpod:

1. Create a new repository in Github using Code's Institute template.
2. Install Django and gunicorn.
3. Install supporting libraries: pip3 install dj_database_url psycopg2
4. Install Cloudinary Libraries: pip3 install dj3-cloudinary-storage
5. Create requirements file: pip3 freeze --local > requirements.txt
6. Create Project bcristus
7. Add to installed apps:
                INSTALLED_APPS = [
                …
                'APP_NAME',
            ]
8. Inside bcristus/settings.py
    - Reference env.py (Note: font in bold is new)
            from pathlib import Path
            import os
            import dj_database_url
            if os.path.isfile("env.py"):
            import env

    - Remove the insecure secret key and replace - links to the SECRET_KEY variable on Heroku.
    - Comment out the old DataBases Section.
    - Add new DATABASES Section.
    - Save all files and Make Migrations.
    - Setup Cloudinary to store media and static files.
    - Link file to the templates directory in Heroku.
    - Change the templates directory to TEMPLATES_DIR
    - Add Heroku Hostname to ALLOWED_HOSTS
    
9. Create media, templates and static folders on top level directory
10. Create a Procfile on the top level directory and add web: gunicorn **bcristus**.wsgi
11. Allauth installed to create user login functionality and updated to requirements.txt
12. Crispyforms installed to allow members comment functionality and updated to requirements.txt.


### In Heroku:

1. Create a new external database
2. Create the Heroku app
3. Attach the database
4. Prepare our environment and settings.py file
5. Get our static and media files stored on Cloudinary.
6. Create new Heroku App.
7. Open the settings tab and Click Reveal Config Vars.
8. Add a Config Var called DATABASE_URL.
9. Add Cloudinary URL to Heroku Config Vars.
10. Add DISABLE_COLLECTSTATIC to Heroku Config Vars.
11. Add Cloudinary Libraries to installed apps
12. Installed summernote and added to requirements via pip3 freeze, as editor for comments in backend.




### In ElephantSQL:

1. Log in to ElephantSQL and creaute an account.
2. Click “Create New Instance”.
3. Select the Tiny Turtle (Free) plan.
4. Click “Select Region”.
5. Check that your details are correct. Then click “Create instance”
6. Return to the ElephantSQL dashboard and click on the database instance name for this project.
7. Copy your ElephantSQL database URL using the Copy icon. It will start with postgres://


### env.py

Inside the project directory there was an env.py file uploaded with the template; inside i did the following changes:

1. Import os library
2. Set environment variables
    - ["DATABASE_URL"]
    - ["SECRET_KEY"] 
    - ["CLOUDINARY_URL"]

## Deploy to Heroku

    Before final deployment, the debug setting in settings.py was set to false;

DEBUG = False

then the DISABLE_COLLECTSTATIC config var in Heroku was removed, connect to github repository and 
deploy from branch, selected GitHub branch and clicked on Deploy button.



## Bugs

### Unfixed:

1. Overall code revision in order to make it more efficient, by loading small scripts without needing to update the whole page, when liking a post for example.


### Fixed

1. I tried to migrate my created models using an ImageField instead CloudinaryField to handle image's post; but terminal requested me to instal "Pillow" for Python to handle images.

2. I wanted to update my model for comments by adding name and email fields, i was getting this error once i tried to migrate; i solve it by typing 1, then true [^1]

3. I was getting an IntegrityError for trying to create an Object without loading properly the image. I changed the field-type in my model and updated the view; comments are stated in the code.


<img src="readme/null1.png">


4. After Crispyforms instalation and setup i wasn't able to render the website; i went thru the documentation and installed $ pip install crispy-bootstrap5 for bootstrap5.... and it worked.

5. I was having an error when  calling the text from the imagePost to be displayed in the Post Card, it showed the text with HTML sintax; however when i call excerpt shows correctly. I found out that i was using the word "content" which turned to be one of hte restricted python words; i change the field name in my model to text; and it worked.


## Features to Improve

- Allow members to create a PDF file from those post card; to be shared or even sent per post upon request.
- The fields in the PostCard, as well as messages could be printed, or not upon request of the member using checkboxes. 
- Members of the community will be able to also comment, edit and like other posts.
- Better placing the information for better UI performance.
- Allow visitors to Signup using social media.
- Allow members to update the post's location using geoTag.
- Visitors will be able to see the statue's location.
- Allow members to share the post images to their own social media.


## Credits

- All media content uploaded to the website belong to me.

## Acknowledgements

- First of all to my family, for allowing me the time to accomplish this classes.
- I'll like to give a credit to [Paul Thomas O'Riordan](https://github.com/paulie-o74) for hosting our weekly thursday meetings, and to "The people from the future", [Tony Albanese](https://github.com/tony-albanese), [Roshna Vakkeel](https://github.com/RoshnaVakkeel) and [Vivi Gnutz](https://github.com/vivignutz).

I found their guidance not just helpful but a "must" condition in order to organize the time and select wich contents to start learning. 

Without them it would have been totally unrealistic to complete this project in this timeframe.
- [Chuck Severance Youtube's channel.](https://www.youtube.com/@ChuckSeverance) With Mr. Severance i took a deeper diving into Database Models and MVC framework's theory.

Notes

[^1]: python3 manage.py makemigrations
You are trying to add a non-nullable field 'name' to comment without a default; we can't do that (the database needs something to populate existing rows)
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option: 1
Please enter the default value now, as valid Python
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
True.

