# Wallet
Simple web application on Django which work same online Wallet

## Functionality of wallet
   - Create Wallet for a User
   - Credit money to wallet 
   - Debit money from wallet
   - Get current Balance

# How to install and run
0. clone project
   ```
   git clone https://github.com/DarshanBPatel/Wallet 
 
   ```
1. Create a virtual environment and launch it:
   ```
   virtualenv -p python3 .venv
   ```
   ```
   source .venv/bin/activate
   ```

2. cd to project root directory of the project wallet
   ```
   cd Wallet
   ```

3. Install requirements:
   ```
   pip install -r requirements.txt
   ```

4. Initialise Database:
   ```
   python manage.py migrate
   ```

5. Now you can start a test server:
   ```
   python manage.py runserver
   ```


