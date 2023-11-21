#include <Python.h>
#include <math.h>
void print_python_float(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

/**
 * print_python_bytes- prints the basic info of a python bytes object
 * @p: pyObject
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = 0, len, i;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		fflush(stdout);
		return;
	}
	PyBytesObject *bytesObj = (PyBytesObject *)p;
	size = bytesObj->ob_base.ob_size;
	printf("  size: %zu\n", size);
	if (size >= 10)
		len = 10;
	else
		len = size + 1;
	printf("  trying string: %s\n", bytesObj->ob_sval);
	printf("  first %zu bytes: ", len);
	for (i = 0; i < len; i++)
	{
		printf("%02hx", (unsigned int)(bytesObj->ob_sval[i] & 0xFF));
		if (i < len - 1)
			printf(" ");
	}

	printf("\n");
	fflush(stdout);
}
/**
 * print_python_float - prints the value of a python float object
 * @p: pyObject
 */
void print_python_float(PyObject *p)
{
	fflush(stdout);
	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		fflush(stdout);
		return;
	}
	PyFloatObject *floatObj = (PyFloatObject *)p;
	char *double_str = PyOS_double_to_string(floatObj->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, Py_DTST_FINITE);
	printf("  value: %s\n", double_str);
	fflush(stdout);
}

/**
 * print_python_list- prints the basic info of a python list object
 * @p: pyObject
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i = 0;


	fflush(stdout);
	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		fflush(stdout);
		return;
	}

	PyListObject *l = (PyListObject *)p;
	size = l->ob_base.ob_size;
	printf("[*] Size of the Python List = %zu\n", size);
	printf("[*] Allocated = %zu\n", l->allocated);
	for (i = 0; i < size; i++)
	{
		printf("Element %zu: %s\n", i, l->ob_item[i]->ob_type->tp_name);
		if (PyBytes_Check(l->ob_item[i]))
			print_python_bytes(l->ob_item[i]);
		else if (PyFloat_Check(l->ob_item[i]))
			print_python_float(l->ob_item[i]);
	}
	fflush(stdout);
}

