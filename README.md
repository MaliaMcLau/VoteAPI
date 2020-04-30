# VoteAPI

**A user should be able to:**
 - register
 - Sign in
 - Cast a vote in a valid election
 - sign in
 - Change display name
 - Change password
 - Create election
 - Enter candidates
 - Set voting format
    - Standard voting
    - Ranking choice voting
 - Edit election
 - Delete a election

Configure election
 - Amount of votes accepted from single user



**Models**

Candidate
 - id
 - name
 - election_id

User
 - id
 - Name
 - Username hash
 - Password hash

Vote
 - id
 - user_id
 - election_id
 - candidate_id

Election
 - id
 - Name
 - Duration
 - Start date
 - type



**Functions**

Candidate
 - Get candidate by id
 - Create candidate
 - Edit candidate
 - Delete candidate
 
User
 - Get user by id
 - Register user
 - Edit user details
 - Delete user
 - Change password
 - Change display name
 
Vote
 - Get vote by id
 - Get vote by user_id
 - Cast vote
 - Must be a check if vote abides by set election rules
 - Edit vote
 - Delete vote
 
Election
 - Get election by id
 - Get list of candidates by election_id
 - Create election
 - Edit election
 - Delete election
