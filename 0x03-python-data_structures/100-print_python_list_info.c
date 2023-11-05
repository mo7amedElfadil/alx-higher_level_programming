#include <Python-3.4.4/Include/Python.h>
#include <Python-3.4.4/Include/listobject.h>
#include <Python-3.4.4/Include/object.h>
/**
 * print_python_list_info - prints the basic info of a python list object
 * @p: pyObject
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, i = 0;
	PyTypeObject *type = p->ob_type;

	if (!PyList_CheckExact(p))
		return;
	PyListObject *l = (PyListObject *)p;

	size = PyList_Size(p);

	printf("[*] Size of the Python List = %zu\n", size);
	printf("[*] Allocated = %zu\n", l->allocated);
	for (i = 0; i < size; i++)
		printf("Element %zu: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);

}

