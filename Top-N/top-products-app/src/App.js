import React, { useEffect, useState } from 'react';
import ProductList from './ProductList';

const App = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://20.244.56.144/test/companies/AMZ/categories/Laptop/products?top=10&minPrice=1&maxPrice=10000', {
          method: 'GET',
          headers: {
            // Add any headers like Authorization token here if required
          },
        });
        const data = await response.json();
        
        console.log(data); // Log the data received from the API
        
        setProducts(data); // Set the data to state
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <h1>Laptop Store</h1>
      <ProductList products={products} />
    </div>
  );
};

export default App;