## WTForms-Adoption Agency

### Step 1: Create Database and Model
- [X] Create a Flask and Flask-SQLAlchemy project, "adopt".
- [X] Create a single model, ***Pet***. This models a pet potentially available for adoption
    - [X] **id****: auto-incrementing integer
    - [X] ***name***: text, required 
    - [X] ***species***: text, required
    - [X] ***photo_url***: text, optional
    - [X] ***age***: integer, optional
    - [X] ***notes***: text, optional
    - [X] ***available***: boolean, required, should default to available
### Step 2: Make Homepage Listing Pets
- [X] The homepage (at route `/`) should list the pets:
    - [X] name
    - [X] show photo, if present
    - [X] display "Available" in bold if the pet is available for adoption
### Step 3: Create Add Pet Form
- [X] Create a form for adding pets. This should use Flask-WTF, and should have the following fields:

    - [X] Pet name
    - [X] Species
    - [X] Photo URL
    - [X] Age
    - [X] Notes
This should be at the URL path `/add`. Add a link to this from the homepage.
### Step 4: Create Handler for Add Pet Form
This should validate the form:
- [X] if it doesn't validate, it should re-render the form
- [X] if it does validate, it should create the new pet, and redirect to the homepage.
This should be a POST request to the URL path `/add`.
### Step 5: Add Validation
- [X] the species should be either "cat", "dog", or "porcupine", *Note: also added hedgehog because why not?*
- [X] the photo URL must be a URL *(but it should still be able to be optional!)*
- [X] the age should be between 0 and 30, if provided.
### Step 6: Add Display/Edit Form
- [X] Make a page that shows some information about the pet:
    - [X] Name
    - [X] Species
    - [X] Photo, if present
    - [X] Age, if present
- [X] It should also show a form that allows us to edit this pets:
    - [X] Photo URL
    - [X] Notes
    - [X] Available
This should be at the URL `/pets/<pet_id>/edit`. Make the homepage link to this.
### Step 7: Handle Edit Form
This should validate the form:
- [X] if it doesn't validate, it should re-render the form
- [X] if it does validate, it should edit the pet
This shold be a POST request to the URL path `/pets/<pet_id>/edit`.
### Step 8: Clean Up Your Code
A critical step for any project is to refactor and clean up code; it's good to do this iteratively, as you work.

Check for:
- [X] function names: good functions names are "verby", like ***show_add_form***
- [X] consistent use of good variable names
- [X] every class or function should have a docstring describing its purpose
- [X] add comments for any parts that would benefit from this
- [X] add a file showing all of the Python requirements for this project
