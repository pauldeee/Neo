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

Scenario	User enables automated Investing
Given			A user is logged in to the system
And					The user had not enabled automated Investing
When			The user clicks the button to enable automated Investing
Then			Automated investing will be enabled for their account

Scenario	AI predicts favorable trade and buys stock
Given			A user is logged in to the system
And					The user has enabled automated Investing
And					The user has sufficient funds in their account
When			The AI evaluates current market conditions and finds a good trade
Then			The AI submits an order to buy the stock

Scenario	AI predicts favorable trade but cannot buy stock
Given			A user is logged in to the system
And					The user has enabled automated Investing
And					The user has insufficient funds in their account
When			The AI evaluates current market conditions and finds a good trade
Then			The AI does not submit an order to buy the stock

Scenario	AI tries submitting purchase order but purchase fails
Given			A user is logged in to the system
And					The user has enabled automated Investing
And					The user has sufficient funds in their account
And					The AI has found a favorable trade
And					The AI tried to submit an order to purchase
When			The purchase order fails
Then			The AI does not retry the order