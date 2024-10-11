CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);

CREATE TABLE accounts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_number TEXT NOT NULL UNIQUE,
    balance REAL NOT NULL DEFAULT 0.0,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    transaction_type TEXT NOT NULL,
    amount REAL NOT NULL,
    date TEXT NOT NULL,
    account_id INTEGER NOT NULL,
    FOREIGN KEY (account_id) REFERENCES accounts (id)
);

CREATE TABLE loans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    loan_type TEXT NOT NULL,
    amount REAL NOT NULL,
    interest_rate REAL NOT NULL,
    start_date TEXT NOT NULL,
    end_date TEXT NOT NULL,
    account_id INTEGER NOT NULL,
    FOREIGN KEY (account_id) REFERENCES accounts (id)
);
