"use client";
import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { addInventory } from "../actions/foodactions";

export function AddInventoryForm({
  onClose,
  data,
}: {
  onClose: () => void;
  data: any;
}) {
  const [product, setProduct] = useState("");
  const [quantity, setQuantity] = useState("");
  const [date, setDate] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    addInventory(product,quantity,date)
    onClose();
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div className="space-y-2">
        <Label htmlFor="product">Choose Product</Label>
        <Select value={product} onValueChange={setProduct} required>
          <SelectTrigger id="product">
            <SelectValue placeholder="Select a Product" />
          </SelectTrigger>
          <SelectContent>
            <SelectContent>
              {data.map((item) => (
                <SelectItem key={item.p_id} value={item.p_id}>
                  {item.name}
                </SelectItem>
              ))}
            </SelectContent>
          </SelectContent>
        </Select>
      </div>
      <div className="space-y-2">
        <Label htmlFor="quantity">Quantity</Label>
        <Input
          id="quantity"
          type="number"
          min="0"
          step="1"
          value={quantity}
          onChange={(e) => setQuantity(e.target.value)}
          required
        />
      </div>
      <div className="flex flex-col space-y-2">
        <Label htmlFor="date">Expiry Date</Label>
        <input type="date" onChange={(e) => setDate(e.target.value)} />
      </div>
      <div className="flex justify-end space-x-2">
        <Button type="button" variant="outline" onClick={onClose}>
          Cancel
        </Button>
        <Button type="submit">Add inventory</Button>
      </div>
    </form>
  );
}
