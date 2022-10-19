Feature: Notifications
As a user
I need to be updated of my stocks' overall performance
So that I can keep abreast of my place in the markets

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
