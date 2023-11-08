#include <Python.h>
/**
 * print_python_bytes- prints the basic info of a python bytes object
 * @p: pyObject
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = 0, len, i;
	char *byte_string;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	PyBytes_AsStringAndSize(p, &byte_string, &size);
	if (size > 10)
		len = 10;
	else
		len = size + 1;
	printf("  size: %zu\n", size);
	printf("  trying string: %s\n", byte_string);
	printf("  first %zu bytes: ", len);
	for (i = 0; i < len; i++)
	{
		printf("%02hx", (unsigned int)(byte_string[i] & 0xFF));
		if (i < len - 1)
			printf(" ");
	}

	printf("\n");

}



/**
 * print_python_list- prints the basic info of a python list object
 * @p: pyObject
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i = 0;

	if (!PyList_CheckExact(p))
		return;
	PyListObject *l = (PyListObject *)p;

	size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zu\n", size);
	printf("[*] Allocated = %zu\n", l->allocated);
	for (i = 0; i < size; i++)
	{
		printf("Element %zu: %s\n", i, l->ob_item[i]->ob_type->tp_name);
		if (PyBytes_Check(l->ob_item[i]))
			print_python_bytes(l->ob_item[i]);
	}
}

