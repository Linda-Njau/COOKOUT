# WELCOME TO COOKOUT!

## Table of Content
- [Inspiration for Cookout](Inspiration for Cookout)
- [Getting Started](Getting started)
 - [Cloning the Repository](Cloning the Repository)
 - [Installing dependencies](Installing dependencies)
 - [Starting the App](Starting the App)
- [Layout](Layout)
- [Tech Stack](Tech Stack)
- [Features](Features)
 - [Authentication](Authentication)
 - [Recipe Creation](Recipe Creation)
 - [Recipe Viewing](Recipe Viewing)
- [Known Bugs](Known Bugs)
- [Future Features](Future Features)
- [Author](Author)

## Inspiration for Cookout
Imagine hosting your friends for dinner, and they're all dying to know the secret behind that mouthwatering salad you whipped up.
 Cookout is the answer. Not only can you impress your guests, but you can also create, discover, 
 and share your favorite recipes with food enthusiasts from around the world. It's time to unlock 
 the potential of your kitchen and embark on a culinary adventure!

Cookout is more than just a recipe app; it's a social network for those obsessed with food. Create a profile and
 connect with fellow foodies who share your passion. From aspiring home cooks to seasoned chefs, 
 Cookout welcomes all skill levels. Whether you're a beginner looking to expand your repertoire or
  a culinary expert eager to showcase your culinary masterpieces, Cookout has you covered
so without further ado, Welcome to Cookout!



![Cookout landing page](https://github.com/Linda-Njau/COOKOUT/blob/master/cookout_screenshots/home_page.png)


## Getting started

To contribute to this project, follow these steps:

### Cloning the Repository
 Clone the repository by running the following command in your terminal or command prompt:
   ``` shell
   git clone https://github.com/Linda-Njau/COOKOUT.git
   ```

### Installing dependencies
Before running the app, make sure you have the required dependencies installed. You can install them using pip:
  ```shell
  pip install -r requirements.txt
  ```

### Starting the App
To start the app, run the following command:
  ```shell
  python3 main.py
   ```
  And with that, you can start contributing!

  ## Layout
Cookout features a user-friendly and intuitive layout, allowing users to effortlessly access all pages from any other page. Whether you're on the Landing page, About page, or browsing recipes, seamless navigation ensures a smooth browsing experience.

For enhanced user engagement, Cookout strategically places `Join Us` buttons on pages that can be accessed without logging in. These buttons serve as prompts, inviting users to become part of the community and enjoy the full benefits of Cookout. Once logged in, users gain access to additional features such as the `New Recipe` and `My Recipe` pages, enabling them to contribute and explore personalized recipe content. 
![user flowchart](https://github.com/Linda-Njau/COOKOUT/blob/master/cookout_screenshots/user%20journey%20flow%20chart.png)
## Tech Stack
Cookout is primarily built using Flask, a lightweight and versatile web framework in Python. The application leverages Flask extensions such as Flask-Login for authentication, Flask-Migrate for seamless database migrations, and Flask-SQLAlchemy for efficient database management. The vibrant and visually appealing frontend of Cookout is achieved through Flask's render-templates, enabling the dynamic generation of HTML pages with colorful and engaging visual elements. Together, this tech stack empowers Cookout to deliver a seamless user experience, robust authentication, efficient database management, and a visually captivating frontend
![tech stack](https://github.com/Linda-Njau/COOKOUT/blob/master/cookout_screenshots/tech%20stack.jpg)

## Features
### Authentication
Cookout incorporates user authentication with dedicated login and signup pages, ensuring a secure and personalized experience. The authentication process is powered by Flask-Login, a robust Flask extension that simplifies user session management and securely verifies user credentials. With Flask-Login, Cookout securely authenticates users and grants access to features like the `New Recipe` and `My Recipes` pages, where users can create and manage their personalized recipe content. This integration guarantees a seamless and secure experience throughout the Cookout application.

![login page](https://github.com/Linda-Njau/COOKOUT/blob/master/cookout%20images/login_page.png)

![signup page](https://github.com/Linda-Njau/COOKOUT/blob/master/cookout_screenshots/login_page.png)

### Recipe Creation
Cookout provides a user-friendly interface for recipe creation. Within the application, users can access a straightforward form to input the details of their recipes. Upon submission, the form data is sent to the designated API endpoint, initiating the necessary database operations. Cookout's Flask backend efficiently processes the data, allowing for the seamless creation and storage of new recipes.

![recipe insp](https://github.com/Linda-Njau/COOKOUT/blob/master/cookout%20images/newrecipe_inspo_page.png)
![recipe form](https://github.com/Linda-Njau/COOKOUT/blob/master/cookout%20images/newrecipe_form_page.png)

### Recipe Viewing
Cookout seamlessly retrieves and presents user-specific recipes through its user-friendly interface. Upon submitting a recipe through the form, the data is securely stored in the database. Leveraging user session management, Cookout efficiently retrieves the relevant recipes associated with the authenticated user. By dynamically rendering the retrieved data within the "My Recipes" section, users can conveniently view and manage their personalized collection of culinary creations. This technical integration ensures a smooth and personalized recipe viewing experience within the Cookout application.
![my recipes](https://github.com/Linda-Njau/COOKOUT/blob/master/cookout%20images/myrecipes_page.png)

## Known Bugs
One known bug in Cookout relates to the delay in displaying flash messages, which can result in messages being shown later than intended. Occasionally, these delayed flash messages may appear after the relevant context or action has passed

## Future Features
- [ ] recipe-sharing capabilities
- [ ] user-profiles and follow/follower feature
- [ ] tag-based discussion forums
- [ ] hidden/private recipes
- [ ] collection feature for recipes

## Author
* fellow foodie: [**Linda Njau**](https://github.com/Linda-Njau)
