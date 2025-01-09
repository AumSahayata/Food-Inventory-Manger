import { SignedIn, UserButton } from "@clerk/nextjs";
import { currentUser } from "@clerk/nextjs/server";

import Products from "../components/products";

export default async function Home() {
  const user = await currentUser();

  return (
    <>
      <Products />
    </>
  );
}
