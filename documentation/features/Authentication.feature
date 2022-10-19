Feature: Authentication
As a user
I need the system to authenticate who I am
So that imposters aren't able to access my account

Scenario	Account creation
Given			A user begins registering for an account
When			The user enters a potential password
Then			The system validates that the password meets security requirements
And					Notifies the user if the password does not meet minimum security requirements

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
