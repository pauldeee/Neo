Feature: Multiplatform Access
As a user
I need to access the system from different platforms
So that I can better keep up to date with my trading

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
