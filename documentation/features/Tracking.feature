Feature: Tracking
As a user
I need to be see real-time market information
So that I can make split-second financial decisions to capitalize on sudden movements

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
