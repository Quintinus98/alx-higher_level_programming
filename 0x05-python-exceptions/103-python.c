#include "main.h"

/**
 * print_python_list - Prints python list
 * @p: A PyObject instance
*/
void print_python_list(PyObject *p)
{
	Py_ssize_t n, allocated, i = 0;
	PyListObject *listObj = (PyListObject *)p;
	PyVarObject *varObj = (PyVarObject *)p;
	const char *item_type;

	n = varObj->ob_size;
	allocated = listObj->allocated;
	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("\t[ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %ld\n", n);
	printf("[*] Allocated = %ld\n", allocated);

	while (i < n)
	{
		item_type = listObj->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, item_type);
		if (strcmp(item_type, "float") == 0)
			print_python_float(listObj->ob_item[i]);
		else if (strcmp(item_type, "bytes") == 0)
			print_python_bytes(listObj->ob_item[i]);
		i++;
	}
}

/**
 * print_python_bytes - Prints python bytes
 * @p: A PyObject instance
*/
void print_python_bytes(PyObject *p)
{
	Py_ssize_t n, i = 0;
	PyBytesObject *byteObj = (PyBytesObject *)p;

	n = ((PyVarObject *)p)->ob_size;
	fflush(stdout);

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("\t[ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("\tsize: %ld\n", n);
	printf("\ttrying string: %s\n", byteObj->ob_sval);

	if (n > 10)
		n = 10;
	else
		n += 1;
	printf("\tfirst %ld bytes: ", n);
	
	while (i < n)
	{
		printf("%02hhx", byteObj->ob_sval[i]);
		if (i == n - 1)
			printf("\n");
		else
			printf(" ");
		i++;
	}
}

/**
 * print_python_float - Prints python float
 * @p: A PyObject instance
*/
void print_python_float(PyObject *p)
{
	char *str = NULL;
	PyFloatObject *floatObj = (PyFloatObject *)p;

	fflush(stdout);
	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("\t[ERROR] Invalid Float Object\n");
		return;
	}
	str = PyOS_double_to_string(floatObj->ob_fval, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("\tvalue: %s\n", str);
	PyMem_FREE(str);
}
