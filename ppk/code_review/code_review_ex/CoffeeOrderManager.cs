using System;
using System.Collections.Generic;

namespace CoffeeOrderManager
{
    // Класс для представления заказа.
    public class Order
    {
        public string? CustomerName { get; set; }
        public string? Drink { get; set; }
        public string? Additions { get; set; }
        public string? Size { get; set; }
        public string? Status { get; set; }

        // Конструктор с параметрами для создания новых заказов.
        public Order(string? customerName, string? drink, string? additions, string? size)
        {
            CustomerName = customerName;
            Drink = drink;
            Additions = additions;
            Size = size;
            Status = "В процессе";
        }

        public override string ToString()
        {
            return $"Имя клиента: {CustomerName}, Напиток: {Drink}, Добавки: {Additions}, Размер: {Size}, Статус: {Status}";
        }
    }

    public class CoffeeOrderManager
    {
        public static void Main(string[] args)
        {
            List<Order> orders = [];

            while (true)
            {
                Console.WriteLine("Добро пожаловать в CoffeeOrderManager!");
                Console.WriteLine("1. Добавить Новый Заказ");
                Console.WriteLine("2. Просмотр Заказов");
                Console.WriteLine("3. Изменить Статус Заказа");
                Console.WriteLine("4. Удалить Заказ");
                Console.WriteLine("5. Выйти");
                string? choice = Console.ReadLine();

                if (choice == "1")
                {
                    AddOrder(orders);
                }
                else if (choice == "2")
                {
                    ViewOrders(orders);
                }
                else if (choice == "3")
                {
                    ChangeOrderStatus(orders);
                }
                else if (choice == "4")
                {
                    DeleteOrder(orders);
                }
                else if (choice == "5")
                {
                    break;
                }
                else
                {
                    Console.WriteLine("Неправильный выбор!");
                }
            }
        }

        public static void AddOrder(List<Order> orders)
        {
            Console.WriteLine("Введите Имя клиента:");
            string? customerName = Console.ReadLine();
            Console.WriteLine("Введите Название напитка:");
            string? drink = Console.ReadLine();
            Console.WriteLine("Введите Добавки к напитку:");
            string? additions = Console.ReadLine();
            Console.WriteLine("Укажите Размер:");
            string? size = Console.ReadLine();

            Order order = new Order(customerName, drink, additions, size);
            orders.Add(order);
            Console.WriteLine("Заказ успешно создан!");
        }

        public static void ViewOrders(List<Order> orders)
        {
            foreach (var order in orders)
            {
                Console.WriteLine(order.ToString());
            }
        }

        public static void ChangeOrderStatus(List<Order> orders)
        {
            Console.WriteLine("Введите Имя клиента для смены статуса заказа:");
            string? customerName = Console.ReadLine();
            foreach (var order in orders)
            {
                if (order.CustomerName == customerName)
                {
                    Console.WriteLine("Укажите новый статус:");
                    order.Status = Console.ReadLine();
                    Console.WriteLine("Статус заказа успешно изменён!");
                    return;
                }
            }
            Console.WriteLine("Заказ не найден!");
        }

        public static void DeleteOrder(List<Order> orders)
        {
            Console.WriteLine("Введите Имя клиента для удаления заказа:");
            string? customerName = Console.ReadLine();
            for (int i = 0; i < orders.Count; i++)
            {
                if (orders[i].CustomerName == customerName)
                {
                    orders.RemoveAt(i);
                    Console.WriteLine("Заказ успешно удалён!");
                    return;
                }
            }
            Console.WriteLine("Заказ не найден!");
        }
    }
}
