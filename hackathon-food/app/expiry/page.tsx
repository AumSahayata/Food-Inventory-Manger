import { currentUser } from "@clerk/nextjs/server";
// const getInventory = async (id) => {
//   console.log(id);
//   const response = await fetch(`${process.env.BASE_URL}/api/inv/${id}`);
//   const data = await response.json();
//   console.log(data);
//   return data;
// };

const getNearExpiryProducts = async (id) => {
  const response = await fetch(
    `${process.env.BASE_URL}/api/inv/expiry/${id}`
  );
  const data = await response.json();
  console.log(data);
  if(data.detail){
    return []
  }
  return data
};

import Expiry from "../components/expiry";

export default async function ExpiryPage() {
    const user = await currentUser();
    const productData = await getNearExpiryProducts(user?.id);

  return (
    <>
      <Expiry data={productData}/>
    </>
  );
}
