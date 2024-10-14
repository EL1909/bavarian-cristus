# Bavarian Cristus

Put ourselves in the user's position
Anticipate the user's wants and needs

Why would a user want to visit our blog?
    - To see photos posted by other users on this particular topic with no hassel
    - To publish their own taken photos
    - To discover places those photos are tagged on and planning trips
    - To share opinions on this images with the community
    - To easily log in using social media profiles

What will make them return
    - The interaction with other members
    - Look for new images

What do i want to see when I visit a blog
    - Images posted from users in the main page
    - Comments from the community on each photo post
    - Map with location of the statue
    - See how many people looked/liked the post
    - Approve/Deny photos before posting
    - Get information about the camera used to get the image..?

What would make me return
    - Answer comments from other community members
    - have a profile with a gallery of my own taken images


How do i develop a blog app that provides all this functionality to a user ? 

Users: All visitors to our domain
Members: registered users authenticated by email
Admin: Super user


EPICS
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



-0-


“Connect Cloudinary,  add config variables Database_url, Secret_key, Cloudinary_url, Port and Disable_collectstatic, and cloudinary to apps;  add staticfiles parameters, allowed hosts and template_dir in settings.py, create media, template and static folders and Procfile”


I tried migrate my created classes but terminal requested me to instal "Pillow" for Python to handle images - did not added via pip3 freeze



installed summernote and added to requirements via pip3 freeze, as editor for comments in posts.


I wanted to update my model for comments by adding name and email fields, i was getting this error once i tried to migrate

python3 manage.py makemigrations
You are trying to add a non-nullable field 'name' to comment without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option: 1
Please enter the default value now, as valid Python
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
>>> True

i solve it by typing 1, then true



15.03.23    - Allauth installed to create user login functionality and updated to requirements.txt
            - Crispyforms installed to allow members comment functionality and updated to requirements.txt. After instalation and setup i wasnt able to render the website; i went thru the documentation and installed $ pip install crispy-bootstrap5 for bootstrap5.... and it worked

16.03.23    - IM having a bug related to the secons screenshot, apparently im not refering to any image post in my views... apparently im trying to post the coment without specifiying the user_id of the commenter... i did dolve it by modifiyng my comment-post view and adding arguments for user and image_post instead post.......

22.03.23    - I need to make the images on landing page to be responsvie as i want; and add comments and location to "postcards" image that im building on my landing

24.03.23    - Im having a bug, when im calling the text from the imagePost to be displayed it shows with HTML sintax; however whn i call excerpt shows correctly.

<img src="media/readme/Text Error.jpg">



29.03.23    - Im having problems with loading the update.html template; when i click the button to upload a new post it doesn't load, shows 404 error; however if i add a / in the url file path, it does load the template, but does not add the new post.



## Classes

## ERD

I will be using three diferent database models for this project: User, ImagePost and Comments,

The User class is the default User class from Django.

The ImagePost class is the key custom class in this project as the main function of the site is for users to share their own taken images.

I found is necessary to have two foreign keys in the Comment model to establish a relationship between the Comment model, the ImagePost model, and the User model.

The image_post foreign key in the Comment model is used to associate each comment with a specific image post. This creates a one-to-many relationship between the ImagePost model and the Comment model, as each ImagePost can have multiple Comment instances associated with it.

The user foreign key in the Comment model is used to track the user who made the comment. This creates a one-to-many relationship between the User model and the Comment model, as each User can have multiple Comment instances associated with it.

<img src="media/readme/EDR-Bavarian-Cristus.png">





VIEWS

<img src="https://share.balsamiq.com/c/6c3j4m96B8F4TvZWwM9xtp.png">





-0-

Bavarian Cristus is a website created by Luciano Fernandez for the purpouse of allowing all people interested in Jesus Christ, that also enjoy to take and share photos, and happen to be residents or visiting Bavaria, to share their pictures and thoughts about images shared by others.

Users of the website will be able to see images and in future versions could also upload their own photos as long as they are taken in Bavaria. 

They will be also able to tag the location of the photo. This will allow visitors to find exactly where the statue is located.

<img src="assets/images/">

In the home page, visitors can have a clear idea of what the website was made for.

the Gallery section contains images uploaded by the developer. in future versions could be possible to comment, like and share images, as well as fin the real location of the statue.

The Post page, is intendet to allow users to share pictures taken by themselves, to be posted in the gallery.

## TESTING 

- The website have been tested in Chrome, Safari and Firefox explorer.
- Navigation, header and menu elemets are confirmed and functional.
- Post section is not properly working yet, only the layout was intendet for this version. 

the website have no unfixed bugs.

## VALIDATOR TESTING

- HTML: No errors returned when passing through the official W3C validator.
- CSS: No errors were found when passing through the official (Jigswaw) validator.
- Accesibility: 

## DEPLOYMENT

The site was deployed to Github Pages. The steps to deploy are as follows:
1. In Github Repository, navigate to the settings tab.
2. From the source section dropdown menu, select the master branch.
3. Once the masterbranch has been selected, the page provide the link to the complete website.

## FEATURES

### Navigation
- Featured at the top of the page, the navigation shows the website name in the left corner BAVARIAN CHRISTUS, that links to the home page.
- In the top-right cornet, users can find the website menu; with three links redirecting to "Home", "Gallery' and "Post" pages respectively, each one has a diferent page.

### Design and colors
- Navigation fonts tend to be sober and respectful; text style contrast with solid background colors.
- Color selection is intended to remember colors at church and in general catholic styles.

## CREDITS

Content
- Noto and Dosis fonts were linked from Google Fonts.
- Icons used for social network links and as decoration in Post submit section are taken from fontawesome.com
- I have utilized [Yoelvis Mulen's](https://www.youtube.com/@YoelvisM/featured) channel in order to discover how to use CSS grids, however im lacking of time with the other projects too and i havent got the time to properly learn it. 

Media
- All text and images belong to the developer.

## Acknowledgement

Actually, im not sure if i did use the grids correctly on my website. I will walk thru this lessons again. 

I am struggling with dates; im having 5 months to do this classes (wich i found amazing), however i haven't got enough time to work in this new knowledge and keeping up with the schedule.


Given the time and with a lot of practice, i'm confident i will become a software developer; even though i have beel failing all projects so far.

