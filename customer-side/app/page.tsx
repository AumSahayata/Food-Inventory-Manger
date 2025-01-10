import Products from "./components/products";

const getProduct = async () => {
  const response = await fetch(
    `http://127.0.0.1:8000/api/inv/products/user_2rOu3Kjmqhx1YjGhdaZkIb8PFUw`
  );
  const data = await response.json();
  console.log(data);
  if (data.detail) {
    return [];
  }
  return data;
};

export default async function ProductGrid() {
  const products = await getProduct();
  return <Products products={products} />;
}
