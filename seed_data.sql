PRAGMA foreign_keys = ON;

-- =========================
-- Insert Clients
-- =========================
INSERT INTO clients (firstname, lastname, email, tel, identification_number)
VALUES
('John', 'Doe', 'john.doe@email.com', '+1234567890', 'ID12345'),
('Jane', 'Smith', 'jane.smith@email.com', '+1987654321', 'ID67890'),
('Mike', 'Brown', 'mike.brown@email.com', '+1122334455', 'ID54321');

-- =========================
-- Insert Cars
-- WorkStatus values:
-- PENDING, IN_PROGRESS, DELIVERED
-- =========================
INSERT INTO cars (
    plate_number,
    year,
    brand,
    model,
    color,
    status,
    image_path,
    client_id
)
VALUES
('ABC-123', 2018, 'Toyota', 'Corolla', 'White', 'PENDING', 'toyota1.jpg', 1),
('XYZ-789', 2020, 'Honda', 'Civic', 'Black', 'IN_PROGRESS', 'honda1.jpg', 1),
('LMN-456', 2017, 'Ford', 'Focus', 'Blue', 'PENDING', 'ford1.jpg', 2),
('QRS-852', 2022, 'BMW', 'X5', 'Gray', 'PENDING', 'bmw1.jpg', 3);
