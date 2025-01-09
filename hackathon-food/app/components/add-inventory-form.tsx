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

import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover";
import { format } from "date-fns";
import { CalendarIcon } from "lucide-react";

import { cn } from "@/lib/utils";

export function AddInventoryForm({ onClose }: { onClose: () => void }) {
  const [product, setProduct] = useState("");
  const [quantity, setQuantity] = useState("");
  const [date, setDate] = useState<Date>();

  const handleSubmit = (e: React.FormEvent) => {
    const datestring = date?.toISOString().split("T")[0];
    e.preventDefault();
    console.log();
    onClose();
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div className="space-y-2">
        <Label htmlFor="category">Choose Product</Label>
        <Select value={product} onValueChange={setProduct} required>
          <SelectTrigger id="category">
            <SelectValue placeholder="Select a category" />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value="electronics">Dairy</SelectItem>
            <SelectItem value="clothing">
              Fruits and Vegetables (1kg)
            </SelectItem>
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
     
      <div className="flex justify-end space-x-2">
        <Button type="button" variant="outline" onClick={onClose}>
          Cancel
        </Button>
        <Button type="submit">Add inventory</Button>
      </div>
    </form>
  );
}
