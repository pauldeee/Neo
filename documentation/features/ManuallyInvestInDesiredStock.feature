Feature: Manually Invest in Desired Stock
As a logged-in user
I need to be able to manually invest in a desired stock
So that I can take control of my financial destiny.

Scenario	View a stock by symbol
Given			A user is logged in
When			The user enters a stock's symbol into the search area
Then			The system returns the data for the most relevant stock

Scenario	View a stock by title
Given			A user is logged in
When			The user enters a stock's name into the search area
Then			The system returns the data for the most relevant stock

Scenario	Search for nonexistent stock
Given			A user is logged in
When			The user enters an invalid stock's name into the search area
Then			The system informs them that the stock cannot be found

Scenario	Buy a stock
Given			A user has selected a stock
And					The user has sufficient funds
When			The user enters a quantity of the stock to buy
Then			The system purchases the stock

Scenario	Cannot buy a stock
Given			A user has selected a stock
And					The user has insufficient funds
When			The user enters a quantity of the stock to buy
Then			The system informs the user that they cannot afford the quantity
