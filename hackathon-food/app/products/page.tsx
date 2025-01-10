import { SignedIn, UserButton } from "@clerk/nextjs";
import { currentUser } from "@clerk/nextjs/server";

import Products from "../components/products";

const getProduct = async (id) => {
  console.log(id);
  const response = await fetch(`${process.env.BASE_URL}/api/inv/all/${id}`);
  const data = await response.json();
  console.log(data);
  if (data.detail) {
    return [];
  }
  return data;
};

export default async function Home() {
  const user = await currentUser();
  const productData = await getProduct(user?.id);
  console.log(productData);
  return (
    <>
      <Products data={productData} />
    </>
  );
}
