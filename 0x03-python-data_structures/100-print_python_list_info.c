#define PY_SSIZE_T_CLEAN
#include <Python.h>

/**
 * print_python_list_info - Prints python list
 * @p: A PyObject instance
*/
void print_python_list_info(PyObject *p)
{
	Py_ssize_t n, allocated, i = 0;
	PyListObject *listObj = (PyListObject *)p;
	PyVarObject *varObj = (PyVarObject *)p;
	const char *item_type;

	n = varObj->ob_size;
	allocated = listObj->allocated;
	fflush(stdout);

	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %ld\n", n);
	printf("[*] Allocated = %ld\n", allocated);

	while (i < n)
	{
		item_type = listObj->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, item_type);
		i++;
	}
}
