#include "Python.h"

/**
 * print_python_list_info - C function that prints some basic
 * info about Python lists.
 * @p: a pointer to a PyObject 
 *
 * Return: some basic info about Python lists.
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *plo;

	int length = PyList_Size(p);

	plo = (PyListObject *)p;
	int allocated = plo->allocated;

	printf("[*] Size of the Python List = %d\n", length);
	printf("[*] Allocated = %d\n", allocated);

/*	for (int i = 0; i < length; i++)
	{
		PyTypeObject *type = 
		printf("Element %d: %s", i, PyList_GetItem(plo,i)->ob_type);
	}*/
}
