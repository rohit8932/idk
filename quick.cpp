#include<iostream>
#include<omp.h>
#include<fstream>
//#include<chrono>
//#include<thread>
//#include "windows.h"
using namespace std;

int partition(int[], int, int);

void quickSort(int arr[], int low, int high) {
	if (low < high) {
		int pivot = partition(arr, low, high);

#pragma omp parallel sections
		{
			//cout << "Max-thread " << omp_get_num_threads() << endl;
#pragma omp section
			{
				//cout << "called by " << omp_get_thread_num() << endl;
				quickSort(arr, low, pivot - 1);
			}
#pragma omp section
			{
				//cout << "called by " << omp_get_thread_num() << endl;;
				quickSort(arr, pivot + 1, high);
			}

		}
	}

}

int partition(int arr[], int low, int high) {
	int pivot = arr[low];
	int pindex = low + 1;

	for (int j = low + 1; j <= high; j++) {
		if (arr[j] < pivot) {
			swap(arr[j], arr[pindex]);
			pindex++;
		}
	}
	pindex--;
	swap(arr[low], arr[pindex]);
	
	return pindex;
}

int main() {
	freopen("input.xml", "r",stdin);
	int arr[20], n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}

	quickSort(arr, 0, n - 1);

	for (int i = 0; i < n; i++)
		cout << arr[i] << " ";

	cout << endl;

	//system("pause");
}
