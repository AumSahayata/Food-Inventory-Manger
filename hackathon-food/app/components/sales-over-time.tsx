"use client";

import { Line } from "react-chartjs-2";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { useState, useEffect } from "react";

// Register chart components
ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

const SalesOverTime = ({ salesData, data }) => {
  const [productChosen, setProductChosen] = useState("");

  useEffect(() => {}, [productChosen]);

  const chartData = {
    labels: salesData.map((entry) => entry.date), // Dates on X-axis
    datasets: [
      {
        label: "Quantity Sold",
        data: salesData.map((entry) => entry.sales_quantity), // Sales quantities on Y-axis
        borderColor: "rgba(75, 192, 192, 1)",
        backgroundColor: "rgba(75, 192, 192, 0.2)",
        borderWidth: 2,
        tension: 0.4, // Smooth curve
      },
    ],
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false, // Allows for height adjustment
    plugins: {
      legend: {
        position: "top",
        labels: {
          font: {
            size: 12, // Smaller legend text
          },
        },
      },
      title: {
        display: true,
        text: "Sales Over Time",
        font: {
          size: 16, // Smaller chart title
        },
      },
    },
    scales: {
      x: {
        title: {
          display: true,
          text: "Date",
          font: {
            size: 12, // Smaller font for X-axis title
          },
        },
        ticks: {
          font: {
            size: 10, // Smaller X-axis ticks
          },
        },
      },
      y: {
        title: {
          display: true,
          text: "Quantity Sold",
          font: {
            size: 12, // Smaller font for Y-axis title
          },
        },
        ticks: {
          font: {
            size: 10, // Smaller Y-axis ticks
          },
        },
      },
    },
  };

  return (
    <>
      <div className="container mx-auto px-4 py-8">
        <h1 className="text-xl font-bold mb-4 text-center">Sales Over Time</h1>
        <div className="relative" style={{ height: "400px" }}>
          <Line data={chartData} options={options} />
        </div>
      </div>
      <div className="flex w-[30%] justify-center mx-auto">
        <Select value={productChosen} onValueChange={setProductChosen} required>
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
      ;
    </>
  );
};

export default SalesOverTime;
