"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { Button } from "@/components/ui/button";

export const Navbar = () => {
  const path = usePathname();

  const navLinks = [
    { href: "/", label: "Inventory" },
    { href: "/products", label: "Products" },
    { href: "/expiry", label: "Nearing Expiry" },
  ];

  return (
    <div
      className="w-64 bg-gray-100 p-6 flex flex-col"
      style={{ height: "calc(100vh - 64px)" }}
    >
      <nav className="space-y-2">
        {navLinks.map((link) => (
          <Button
            key={link.href}
            asChild
            variant="ghost"
            className={`w-full justify-start ${
              path === link.href
                ? "bg-green-200 text-green-800 font-semibold"
                : "text-gray-700 hover:bg-gray-200"
            }`}
          >
            <Link href={link.href}>{link.label}</Link>
          </Button>
        ))}
      </nav>
    </div>
  );
};
