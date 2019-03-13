# GRAM-INSTA
*BY OKALL VIVIAN*

## Description

This is a simple clone of instagram that works similar to instagram itself.


## User Stories
Through this application a user is able to:

1. Sign in to the application to start using.


2. Upload my pictures to the application.


3. See profile with all pictures.


4. See posted pictures by different users


5. Update his/her profile


6. The application is responsive in all screen types


## Setup/Installation Requirements
To start using this project use the following commands:

* `git clone https://github.com/Okalll/gram-insta.git`
* `cd Gallery`
* `atom .`
* `code . `(this is if Visual Studio Code is your preferred text editor)

To run this program
* run this command lines in your terminal:
* `python manage.py runserver`
* access the application on this localhost address `http://127.0.0.1:8000`

## Prerequisites
You need the following to work on the project:

`-Python version 3.6`

`-Django 2.0`

`-Pip`

`virtual`environment

`-A text  Editor`


##Behaviour Driven Development

|  Behaviour |  Input  |  Output |
|------------|---------|---------|
| The program should displays the sign-up form first | credentials of the user | A user is created |
| The program should send an activation email  | Click the link sent in your email | Redirected to log-in again for proper authentication |
|The program should direct the user to their timeline page when logged in | Login as a user | Redirected to the timeline page with photos posted by other users |
|The program should add a like or remove a like when the heart icon is clicked on | Click on the heart icon | Click on the heart icon | A like is added if it wasn't added before else it is removed |
|The program should have a comment section on an image | Write on the comment section | The comment will appear on the image| 

## Link to Live Website
https://viv-gram.herokuapp.com/

## Technologies used
- Python 3.6
- HTML
- Bootstrap 4
- JavaScript
- Heroku
- Postgresql

## License
MIT License

Copyright (c) 2018 Okall Vivian

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sub-license, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.