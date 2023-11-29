#include <Python.h>

void print_python_string(PyObject *p);

/**
 * print_python_string - prints the basic info of a python string object
 * @p: pyObject
 */

void print_python_string(PyObject *p)
{
	Py_ssize_t size = 0, len, i;


	fflush(stdout);
	printf("[.] string object info\n");
	/* if (!print_python_string(p)) */
	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		fflush(stdout);
		return;
	}
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else if (PyUnicode_IS_COMPACT(p))
		printf("  type: compact unicode object\n");
	printf("  length: %zu\n", PyUnicode_GET_SIZE(p));
	printf("  value: %s\n", PyUnicode_AsUTF8(p));
	fflush(stdout);
}

