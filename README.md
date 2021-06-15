# Pitches

> A web application that allows the users to post pitches, comment and vote on pitches.

## Author

> By **Yegon C Johnstone**

> ---

## Description

> This is a web application that allows various users to submit a short pitch. Users can also be able to view other pitches from different categories (Pick-up Lines, Interview Pitches, Product Pitches, Promotion Pitches), comment and vote. For a user to do any of that, they need to have registered.

## User Stories

As a user I would like:

> - to view the different categories.
> - to see the pitches other people have posted.
> - to comment on the different pitches and leave feedback.
> - to submit a pitch in any category.
> - to vote on the pitch they liked and give it a downvote or upvote.

## How to use it

> - Internet connection
> - Click https://pitches-zone.herokuapp.com/) <br/>
>   or <br/>
> - Copy https://pitches-zone.herokuapp.com/) and Paste the link on your prefered browser

## How it works

> - A user needs to sign up
> - A user needs to sign in to vote and post pitches
> - A user can also create categories and post pitches within the application

## Technologies Used

> - Python3.8
> - Flask framework
> - Bootstrap
> - PostgreSQL

## Setup/Installation Requirements

### Prerequisites

> - Internet access
> - `git clone https://github.com/jwy951/Pitches-App.git`
> - `cd Pitches`

#### To install a virtual environment

> - `python3.8 -m venv virtual`
> - `source venv/bin/activate`

#### To install all dependencies

> - `python3.8 -m pip install -r requirements.txt`

#### To change the config_name parameter from 'production' to 'development'

> - Inside the manage.py module i.e:- `app = create_app('production')` should be `app = create_app('development')`
> - Then run `python3.8 manage.py server` to get the app running navigate to `http://127.0.0.1:5000/` and it will open in your browser

## Dependancy Installments

> - pip install python3.8
> - pip install flask
> - pip install flask-bootstrap
> - pip install flask-script
> - pip install flask-wtf
> - pip install flask-migrate
> - pip install flask-login
> - pip install Flask-Mail
> - pip install flask-uploads

## Specifications

> - To see the projects specifications refer to the [SPECS.md](SPECS.md) file for more details.

## Known Bugs

> It does not have bugs.But if any problems should occur, email me at devsarahmarion@gmail.com

## Support and Contact Details

> You can reach out to me at johnstoneshylock@gmail.com
> for Reviews, Advice, Collaborations and Comments

## Licence

> MIT License

> Copyright (c) 2021 **Dev Yegon**

> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
> in the Software without restriction, including without limitation the rights
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the Software is
> furnished to do so, subject to the following conditions:

> The above copyright notice and this permission notice shall be included in all
> copies or substantial portions of the Software.

> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
> SOFTWARE.

> ---
