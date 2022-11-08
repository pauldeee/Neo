Feature: Enable Automated Investing
As a user
I need to be see what-if information for given investments and have the system invest on my behalf
So that I can calculate potential trading options for the future and capitalize on market movements while I'm out living life.

Scenario	User views calculated investment for a given stock if bought and sold particular dates
Given			A user is logged in to the system
And					The user has chosen a stock to evaluate
When			The user enters a historical date from which to estimate
And					The user enters a quantity to have purchased
And					The user enters a historical date from which to end estimation
Then			The system will calculate and display the potential outcomes of their speculative stock

Scenario	User views calculated investment for a given stock if bought on a particular date
Given			A user is logged in to the system
And					The user has chosen a stock to evaluate
When			The user enters a historical date from which to estimate
And					The user enters a quantity to have purchased
And					The user does not enter a historical date from which to end estimation
Then			The system will calculate and display the potential state of their speculative stock

Scenario	User enters invalid date
Given			A user is logged in to the system
And					The user has chosen a stock to evaluate
When			The user enters an invalid historical date from which to estimate
Then			The system will prevent the user from continuing this analysis until the date is fixed

Scenario	User enters invalid quantity
Given			A user is logged in to the system
And					The user has chosen a stock to evaluate
When			The user enters a historical date from which to estimate
And					The user enters an invalid quantity
Then			The system will prevent the user from continuing this analysis until the quantity is fixed
