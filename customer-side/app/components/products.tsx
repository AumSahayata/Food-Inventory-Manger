"use client";
import { ProductCard } from "./productCard";

const Products = ({ products }) => {
  //   return (
  // <div className="container mx-auto px-4 py-8">
  //   <h1 className="text-3xl font-bold mb-8 text-center">Products</h1>
  //   <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-6">
  //     {products.map((product) => (
  //       <div
  //         key={product.p_id}
  //         className="bg-white rounded-lg shadow-md overflow-hidden"
  //       >
  //         <Image
  //           src={image}
  //           alt={product.name}
  //           width={200}
  //           height={200}
  //           className="w-full h-48 object-cover"
  //         />
  //         <div className="p-4">
  //           <h2 className="text-xl font-semibold mb-2">{product.name}</h2>
  //           <p className="text-gray-600 mb-4">
  //             &#8377;{product.price.toFixed(2)}
  //           </p>

  //           <button
  //             className="w-full bg-black text-white rounded-md p-4 transition duration-300 ease-in-out
  //          hover:bg-gray-800 focus:ring-2 focus:ring-offset-2 focus:ring-gray-600 active:scale-95"
  //             onClick={() => onPurchase(product.p_id)}
  //           >
  //             Buy Now
  //           </button>
  //         </div>
  //       </div>
  //     ))}
  //   </div>
  // </div>
  const discountedProducts = products.filter(
    (product) => product.is_discounted
  );
  const regularProducts = products.filter((product) => !product.is_discounted);

  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold mb-8 text-center">Our Products</h1>

      {discountedProducts.length > 0 && (
        <section className="mb-12">
          <h2 className="text-2xl font-bold mb-4">Hot Deals</h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-6">
            {discountedProducts.map((product) => (
              <ProductCard key={product.p_id} product={product} />
            ))}
          </div>
        </section>
      )}

      <section>
        <h2 className="text-2xl font-bold mb-4">All Products</h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-6">
          {regularProducts.map((product) => (
            <ProductCard key={product.p_id} product={product} />
          ))}
        </div>
      </section>
    </div>
  );
  //   );
};

export default Products;
