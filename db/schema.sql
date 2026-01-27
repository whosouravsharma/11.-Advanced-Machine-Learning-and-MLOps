-- Files
CREATE TABLE uploaded_files (
    file_id CHAR(36) PRIMARY KEY,
    original_filename VARCHAR(255),
    stored_path VARCHAR(500),
    uploaded_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Companies table
CREATE TABLE companies (
    company_id CHAR(36) PRIMARY KEY,
    company_name NVARCHAR(255),
    currency CHAR(3),
    fiscal_year INT,
    source_file NVARCHAR(255),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Financial statements
CREATE TABLE financial_statements (
    statement_id CHAR(36) PRIMARY KEY,
    company_id CHAR(36) NOT NULL,
    statement_type VARCHAR(20), -- PNL, BALANCE_SHEET, CASH_FLOW
    line_item NVARCHAR(255),
    period NVARCHAR(50),
    amount DECIMAL(18,2),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_company
        FOREIGN KEY (company_id) REFERENCES companies(company_id)
);

CREATE TABLE financial_facts_raw (
    fact_id CHAR(36) PRIMARY KEY,
    company_id CHAR(36) NOT NULL,
    source_file_id CHAR(36) NOT NULL,

    statement_type VARCHAR(20) NOT NULL,
    -- PNL | BALANCE_SHEET | CASH_FLOW

    line_item VARCHAR(255) NOT NULL,
    raw_line_item VARCHAR(255),

    amount DECIMAL(18,2),

    -- ---- PERIOD INTELLIGENCE ----
    period_type VARCHAR(10) NOT NULL,
    -- MONTH | QUARTER | YEAR

    fiscal_year INT NULL,
    quarter INT NULL,
    month INT NULL,

    period_label VARCHAR(50) NOT NULL,
    -- "Jan-24", "Q2 FY25", "FY24"

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);


-- Indexes
CREATE INDEX idx_statement_type ON financial_statements(statement_type);
CREATE INDEX idx_company_id ON financial_statements(company_id);
