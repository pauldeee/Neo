Feature: Research
As a user
I need the system to provide accurate information about stocks on the dashboard
So that I can make informed decisions while using the system.

Scenario	Account creation with bad password
Given			A user begins registering for an account
When			The user enters an insufficient password
Then			The system validates that the password does not meet security requirements
And					Informs the user that the password is not strong enough

Scenario	Account creation with duplicate username
Given			A user begins registering for an account
When			The user enters a username that already exists in the system
Then			The system validates that the username is not unique
And					Informs the user that their desired username is already taken

Scenario	Account creation with valid data
Given			A user begins registering for an account
When			The user enters a valid username and password
Then			The system validates that the credentials are okay
And					Finishes creating account

Scenario	Login attempt to the system
Given			A user has an account in the system
When			A user accesses the system and enters their login information
Then			The system validates their credentials
And					Prompts the user to verify with multifactor Authentication

Scenario	Multifactor authentication success
Given			A user has started authentication procedures
When			The user enters their correct multifactor authentication code
Then			The system validates the code
And					Presents the user with the home page

Scenario	Multifactor authentication failure
Given			A user has started authentication procedures
When			The user enters their incorrect multifactor authentication code
Then			The system tries to validate the code
And					Notifies the user that their login attempt failed
And					Redirects the user back to the login page

Scenario	User accesses FAQ
When			The user opens the FAQ
Then			The system displays helpful information

Scenario	System access via smartphone
Given			A user has an account in the system
And					The user has a smartphone with an Internet connection
When			The user accesses the system via their mobile web browser
Then			The system presents the user with an experience optimized for their device

Scenario	System access via desktop/laptop
Given			A user has an account in the system
And					The user has a desktop/laptop with an Internet connection
When			The user accesses the system via their web browser
Then			The system presents the user with an experience optimized for their device

Scenario	User opens historical information for a stock
Given			A user is logged in to the system
And					The user has chosen a stock to research
When			The user requests historical stock information
Then			The system will display past data for that stock

Scenario	Newsfeed usage
Given			A user is logged in to the system
When			The user accesses the newsfeed area in the system
Then			Tables/graphs of stock trends and possibilities will be presented

Scenario	Daily outliers usage
Given			A user is logged in to the system
When			The user accesses the newsfeed area in the system
Then			The system will display a table of most significant outliers in the market for the day

Scenario	Monthly outliers usage
Given			A user is logged in to the system
When			The user accesses the newsfeed area in the system
Then			The system will display a table of most significant outliers in the market for the month

Scenario	Yearly outliers usage
Given			A user is logged in to the system
When			The user accesses the newsfeed area in the system
Then			The system will display a table of most significant outliers in the market for the year
