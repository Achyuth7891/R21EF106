import React from 'react';

const ProductList = ({ products }) => {
  return (
    <div>
      <h2>List of Laptops</h2>
      <ul>
        {products.map((product, index) => (
          <li key={index}>
            <p>Product Name: {product.productName}</p>
            <p>Price: {product.price}</p>
            <p>Rating: {product.rating}</p>
            <p>Discount: {product.discount}%</p>
            <p>Availability: {product.availability}</p>
            <hr />
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ProductList;