Feature: Manually Sell an Owned Stock
As a logged-in user
I need to be able to manually sell my stocks
So that I can take control of my financial destiny.

Scenario	View owned stocks
When			The user opens their account page
Then			The system displays their owned stocks

Scenario	See owned stock details
Given			The user owns a quantity of a stock
And					The user is on their account page
When			The user selects their holding in that stock
Then			The system displays details for that stock

Scenario	Sell a stock
Given			A user has selected a stock
And					The user owns a quantity of that stock
When			The user enters a quantity of the stock to sell
Then			The system sells the stock

Scenario	Cannot sell unowned stock
Given			A user has selected a stock
And					The user does not own the stock
When			The user enters a quantity of the stock to sell
Then			The system informs the user that they do not own the stock

Scenario	Cannot sell more of a stock than is owned
Given			A user has selected a stock
And					The user owns 100 shares of that stock
When			The user specifies to sell 101 shares of the stock
Then			The system informs the user that they cannot sell more than they own
