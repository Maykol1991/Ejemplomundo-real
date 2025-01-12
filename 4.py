/ See https://aka.ms/new-console-template for more information
using System;
using System.Collections.Generic;
using System.Linq;

namespace AgendaTelefonica
{
    // Clase que representa un contacto
    public class Contacto
    {
        public string Nombre { get; set; }
        public string Telefono { get; set; }

        public Contacto(string nombre, string telefono)
        {
            Nombre = nombre;
            Telefono = telefono;
        }

        public override string ToString()
        {
            return $"Nombre: {Nombre}, Teléfono: {Telefono}";
        }
    }

    // Clase que gestiona la agenda telefónica
    public class Agenda
    {
        private List<Contacto> contactos;

        public Agenda()
        {
            contactos = new List<Contacto>();
        }

        // Agregar un nuevo contacto
        public void AgregarContacto(string nombre, string telefono)
        {
            contactos.Add(new Contacto(nombre, telefono));
            Console.WriteLine("Contacto agregado exitosamente.");
        }

        // Buscar un contacto por nombre
        public void BuscarContacto(string nombre)
        {
            var resultados = contactos.Where(c => c.Nombre.Contains(nombre, StringComparison.OrdinalIgnoreCase)).ToList();
            if (resultados.Count > 0)
            {
                Console.WriteLine("Contactos encontrados:");
                resultados.ForEach(c => Console.WriteLine(c));
            }
            else
            {
                Console.WriteLine("No se encontraron contactos con ese nombre.");
            }
        }

        // Modificar un contacto existente
        public void ModificarContacto(string nombre, string nuevoNombre, string nuevoTelefono)
        {
            var contacto = contactos.FirstOrDefault(c => c.Nombre.Equals(nombre, StringComparison.OrdinalIgnoreCase));
            if (contacto != null)
            {
                contacto.Nombre = nuevoNombre;
                contacto.Telefono = nuevoTelefono;
                Console.WriteLine("Contacto modificado exitosamente.");
            }
            else
            {
                Console.WriteLine("Contacto no encontrado.");
            }
        }

        // Eliminar un contacto por nombre
        public void EliminarContacto(string nombre)
        {
            var contacto = contactos.FirstOrDefault(c => c.Nombre.Equals(nombre, StringComparison.OrdinalIgnoreCase));
            if (contacto != null)
            {
                contactos.Remove(contacto);
                Console.WriteLine("Contacto eliminado exitosamente.");
            }
            else
            {
                Console.WriteLine("Contacto no encontrado.");
            }
        }

        // Mostrar todos los contactos
        public void MostrarContactos()
        {
            if (contactos.Count > 0)
            {
                Console.WriteLine("Lista de contactos:");
                foreach (var contacto in contactos.OrderBy(c => c.Nombre))
                {
                    Console.WriteLine(contacto);
                }
            }
            else
            {
                Console.WriteLine("No hay contactos en la agenda.");
            }
        }

        // Generar reporte de la agenda
        public void GenerarReporte()
        {
            Console.WriteLine("\n--- Reporte de Agenda Telefónica ---");
            Console.WriteLine($"Total de contactos: {contactos.Count}");
            Console.WriteLine("Contactos ordenados alfabéticamente:");
            MostrarContactos();
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Agenda agenda = new Agenda();
            int opcion;

            do
            {
                Console.WriteLine("\n--- Agenda Telefónica ---");
                Console.WriteLine("1. Agregar Contacto");
                Console.WriteLine("2. Buscar Contacto");
                Console.WriteLine("3. Modificar Contacto");
                Console.WriteLine("4. Eliminar Contacto");
                Console.WriteLine("5. Mostrar Contactos");
                Console.WriteLine("6. Generar Reporte");
                Console.WriteLine("7. Salir");
                Console.Write("Seleccione una opción: ");

                if (int.TryParse(Console.ReadLine(), out opcion))
                {
                    switch (opcion)
                    {
                        case 1:
                            Console.Write("Ingrese el nombre: ");
                            string nombre = Console.ReadLine();
                            Console.Write("Ingrese el teléfono: ");
                            string telefono = Console.ReadLine();
                            agenda.AgregarContacto(nombre, telefono);
                            break;
                        case 2:
                            Console.Write("Ingrese el nombre a buscar: ");
                            string nombreBusqueda = Console.ReadLine();
                            agenda.BuscarContacto(nombreBusqueda);
                            break;
                        case 3:
                            Console.Write("Ingrese el nombre del contacto a modificar: ");
                            string nombreModificar = Console.ReadLine();
                            Console.Write("Ingrese el nuevo nombre: ");
                            string nuevoNombre = Console.ReadLine();
                            Console.Write("Ingrese el nuevo teléfono: ");
                            string nuevoTelefono = Console.ReadLine();
                            agenda.ModificarContacto(nombreModificar, nuevoNombre, nuevoTelefono);
                            break;
                        case 4:
                            Console.Write("Ingrese el nombre del contacto a eliminar: ");
                            string nombreEliminar = Console.ReadLine();
                            agenda.EliminarContacto(nombreEliminar);
                            break;
                        case 5:
                            agenda.MostrarContactos();
                            break;
                        case 6:
                            agenda.GenerarReporte();
                            break;
                        case 7:
                            Console.WriteLine("Saliendo de la agenda telefónica.");
                            break;
                        default:
                            Console.WriteLine("Opción no válida. Intente de nuevo.");
                            break;
                    }
                }
                else
                {
                    Console.WriteLine("Por favor, ingrese un número válido.");
                }

            } while (opcion != 7);
        }
    }
}