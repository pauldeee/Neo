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

Scenario	User enables automated investing while the market is open
Given			A user is logged in to the system
And					The user had not enabled automated Investing
And					The market is currently open
When			The user clicks the button to enable automated Investing
Then			Automated investing will be enabled for their account
And					Automated investing will be queued to begin after market close

Scenario	User enables automated investing while market is closed
Given			A user is logged in to the system
And					The user had not enabled automated Investing
And					The market is currently closed
When			The user clicks the button to enable automated Investing
Then			Automated investing will be enabled for their account
And					Automated investing will be queued to run with next batch

Scenario	AI predicts favorable trade and buys stock
Given			A user is logged in to the system
And					The user has enabled automated Investing
And					The user has sufficient funds in their account
And					The markets are currently closed
When			The AI evaluates current market conditions and finds a good trade
Then			The AI submits an order to buy the stock at market open

Scenario	AI predicts favorable trade but cannot buy stock
Given			A user is logged in to the system
And					The user has enabled automated Investing
And					The user has insufficient funds in their account
And					The markets are currently closed
When			The AI evaluates current market conditions and finds a good trade
Then			The AI does not submit an order to buy the stock

Scenario	AI tries submitting purchase order but purchase fails
Given			A user is logged in to the system
And					The user has enabled automated Investing
And					The user has sufficient funds in their account
And					The markets are currently closed
And					The AI has found a favorable trade
And					The AI tried to submit an order to purchase
When			The purchase order fails
Then			The AI does not retry the order

Scenario	AI submits sell orders at market close
Given			A user is logged in to the system
And					The user has enabled automated Investing
And					The AI placed buy orders earlier in the day
When			The markets will close in five minutes
Then			The AI places sell orders for the stocks it bought