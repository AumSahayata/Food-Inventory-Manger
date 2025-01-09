import { SignedIn, UserButton } from "@clerk/nextjs";
import { currentUser } from "@clerk/nextjs/server";

import Dashboard from "./components/dashboard";

const getInventory = async (id) => {
  console.log(id);
  const response = await fetch(`${process.env.BASE_URL}/api/inv/${id}`);
  const data = await response.json();
  console.log(data);
  return data;
};

const getProduct = async (id) => {
  console.log(id);
  const response = await fetch(
    `${process.env.BASE_URL}/api/inv/products/${id}`
  );
  const data = await response.json();
  console.log(data);
  return data;
};

export default async function Home() {
  const user = await currentUser();
  const productData = await getProduct(user?.id);
  const inventoryData = await getInventory(user?.id);
  return (
    <>
      <Dashboard data={productData} inven={inventoryData} />
    </>
  );
}
