Feature: Input
As a user
I need to be able to use the system frequently or infrequently
So that I can fit usage of the system to my lifestyle

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
