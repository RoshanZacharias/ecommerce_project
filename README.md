# ecommerce_project
This Django Rest Framework (DRF) project manages customers, orders, and products, providing a flexible and validated e-commerce API.

## API Endpoints

### Customers

- List all customers: `GET /api/customers/`
- Create/Update customer: `POST/PUT /api/customers/<id>/`

### Products

- List all products: `GET /api/products/`
- Create a new product: `POST /api/products/`

### Orders

- List all orders: `GET /api/orders/`
- Create/Edit order: `POST/PUT /api/orders/<id>/`
- List orders by products: `GET /api/orders/?products=Book,Pen`
- List orders by customer: `GET /api/orders/?customer=Sam`

## Validations

- Unique customer and product names
- Weight <= 25kg, positive decimal
- Order cumulative weight < 150kg
- Order date not in the past.


## Usage

1. Clone the repository:

   ```bash
   https://github.com/RoshanZacharias/ecommerce_project.git
