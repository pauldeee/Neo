Feature: Set Up Notifications
As a user
I need to be able to use the system frequently or infrequently
So that I can fit usage of the system to my lifestyle.

Scenario	Opt-in to notifications
Given			A user is logged in to the system
And					The user has not opted-in to notifications
When			The user navigates to the notifications section
And					Selects to enable notifications
Then			The system will record that the user wants to receive notifications

Scenario	Opt-out of notifications
Given			A user is logged in to the system
And					The user has opted-in to notifications
When			The user navigates to the notifications section
And					Selects to disable notifications
Then			The system will record that the user does not want to receive notifications

Scenario	Notification after significant inactive usage
Given			A user has an account in the system
And					The user has not actively monitored the system for a significant period of time
And					The user has active investments
And					The user has opted-in to notifications
When			The system detects a significant period of time has elapsed
Then			The system will notify the user with a report of overall performance

Scenario	No notifications after opt-out
Given			A user has an account in the system
And					The user has opted-in to notifications
When			The user opts-out of notifications
And					The system detects a significant period of time has elapsed
Then			The system will not send a notification to the user

Scenario	A significant movement has occurred in a tracked stock
Given			A user has an account in the system
And					The user has designated a particular stock as tracked
And					The user has opted-in to notifications
When			The system detects a noteworthy change in the stock
Then			The system will notify the user regarding the event

Scenario	User accesses the system frequently
Given			A user has an account with the system
And					The user accesses the system frequently
When			The user accesses the system
Then			The system will display relevant, real-time information and potential options for new investment decisions

Scenario	User accesses the system infrequently
Given			A user has an account with the system
And					The user accesses the system infrequently
When			The user accesses the system
Then			The system will display longer-term trends and information about their investments

Scenario	User accesses the system rarely
Given			A user has an account with the system
And					The user accesses the system rarely
When			The user accesses the system
Then			The system will display investment summaries and promote features of the system

Scenario	User tracks a stock
Given			A user is logged in to the system
And					The user has not designated a particular stock as tracked
When			The user selects the stock for tracking
Then			The system will save their choice for tracking

Scenario	A user views list of tracked stocks
Given			A user is logged in to the system
And					The user has designated any as tracked
When			The user navigates to the section denoting tracked stocks
Then			The system will display a list of all of the stocks that the user has marked for tracking

Scenario	User stops tracking a stock
Given			A user is logged in to the system
And					The user has designated a particular stock as tracked
When			The user selects the stock to stop tracking
Then			The system will save their choice for not tracking
