Feature: History
As a user
I need to be see historical market information for a stock
So that I can make informed financial decisions to capitalize on long term trends

Scenario	User opens historical information for stock
Given			A user is logged in to the system
And					The user has chosen a stock to research
When			The user requests historical stock information
Then			The system will display past data for that stock
