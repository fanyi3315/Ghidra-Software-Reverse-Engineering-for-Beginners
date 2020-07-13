from ghidra.program.model.symbol import SourceType
from ghidra.program.model.address.Address import *
from struct import pack

exports = set(['GetThreadPreferredUILanguages', 'ReleaseMutex', 'InterlockedPopEntrySList', 'AddVectoredContinueHandler', 'ClosePrivateNamespace', 'SignalObjectAndWait', 'SetConsoleOS2OemFormat', 'DisconnectNamedPipe', 'uaw_wcslen', 'BaseCheckElevation', 'GetNumaAvailableMemoryNode', 'GetThreadGroupAffinity', 'LeaveCriticalSectionWhenCallbackReturns', 'CheckNameLegalDOS8Dot3W', 'GetLogicalDrives', 'CheckNameLegalDOS8Dot3A', 'EnumResourceLanguagesW', 'BasepAllocateActivationContextActivationBlock', 'CreateSemaphoreExW', 'K32EnumPageFilesW', 'TermsrvGetWindowsDirectoryA', 'CreateSemaphoreExA', 'WaitForSingleObject', 'EnumResourceLanguagesA', 'TermsrvGetWindowsDirectoryW', 'K32EnumPageFilesA', 'GetProcessAffinityMask', 'QueryUmsThreadInformation', 'ReleaseMutexWhenCallbackReturns', 'TlsGetValue', 'EnumSystemGeoNames', 'GetSystemTime', 'SetFileIoOverlappedRange', 'GetUILanguageInfo', 'SetConsoleActiveScreenBuffer', 'BasepConstructSxsCreateProcessMessage', 'SetFileAttributesTransactedW', 'QuirkGetData2Worker', 'RegisterConsoleIME', 'DeleteTimerQueueTimer', 'TzSpecificLocalTimeToSystemTimeEx', 'CreateProcessAsUserA', 'TermsrvOpenUserClasses', 'MoveFileTransactedA', 'QuirkIsEnabledWorker', 'MoveFileTransactedW', 'DecodePointer', 'CreateProcessAsUserW', 'GlobalMemoryStatus', 'SetTimeZoneInformation', 'GetConsoleNlsMode', 'ReadThreadProfilingData', 'GetNamedPipeAttribute', 'CreateJobSet', 'DisableThreadLibraryCalls', 'SetFileApisToANSI', 'WaitForThreadpoolWorkCallbacks', 'GetConsoleAliasesW', 'CreateMutexExW', 'OpenProcess', 'SetProcessPriorityBoost', 'RegisterWowExec', 'GlobalLock', 'GetConsoleAliasesA', 'CreateMutexExA', 'GetCurrentProcessorNumberEx', 'EnumResourceNamesW', 'QueryThreadpoolStackInformation', 'SetFirmwareEnvironmentVariableExW', 'Wow64GetThreadContext', 'EnumResourceNamesA', 'SetFirmwareEnvironmentVariableExA', 'GetFileInformationByHandleEx', 'WerRegisterRuntimeExceptionModuleWorker', 'EnumResourceLanguagesExW', 'GetLongPathNameTransactedA', 'EnumResourceLanguagesExA', 'GetNamedPipeClientProcessId', 'VirtualAllocEx', 'UnregisterWaitEx', 'Process32NextW', 'LockFile', 'ReleaseSemaphoreWhenCallbackReturns', 'CompareStringEx', 'VerifyScripts', 'SetFileTime', 'MapUserPhysicalPages', 'PowerCreateRequest', 'EnumResourceTypesA', 'DisassociateCurrentThreadFromCallback', 'HeapUnlock', 'HeapCompact', 'EnumTimeFormatsW', 'EnumResourceTypesW', 'GetACP', 'QueryProcessAffinityUpdateMode', 'QueryIdleProcessorCycleTime', 'ReleaseActCtxWorker', 'GetTimeZoneInformationForYear', 'SetMailslotInfo', 'GetNextUmsListItem', 'GetVolumePathNameW', 'AreFileApisANSI', 'UmsThreadYield', 'DeactivateActCtx', 'QuirkIsEnabledForProcessWorker', 'GetVolumePathNameA', 'GetConsoleMode', 'OpenPrivateNamespaceA', 'ClearCommBreak', 'OpenPrivateNamespaceW', 'GetThreadContext', 'RegCopyTreeW', 'MoveFileWithProgressW', 'RtlRestoreContext', 'CopyFileExW', 'GetLogicalDriveStringsA', 'InterlockedPushEntrySList', 'GetCalendarDaysInMonth', 'AddRefActCtxWorker', 'GetLogicalDriveStringsW', 'CallbackMayRunLong', 'CreateThreadpoolWait', 'CancelSynchronousIo', 'K32GetModuleFileNameExW', 'FlushFileBuffers', 'K32GetModuleFileNameExA', 'GetNumaProcessorNode', 'GetSystemTimePreciseAsFileTime', 'BasepAppContainerEnvironmentExtension', 'GetCalendarInfoW', 'SetEventWhenCallbackReturns', 'GetCurrentApplicationUserModelId', 'MultiByteToWideChar', 'SetFilePointerEx', 'TryAcquireSRWLockExclusive', 'GetCalendarInfoA', 'CreateMutexA', 'RegLoadKeyA', 'SetCachedSigningLevel', 'VirtualUnlock', 'MoveFileExW', 'EnumCalendarInfoExEx', 'CreateMutexW', 'RegLoadKeyW', 'FindNLSStringEx', 'BasepReleaseAppXContext', 'MoveFileExA', 'K32EmptyWorkingSet', 'DosPathToSessionPathW', 'SearchPathW', 'SearchPathA', 'VirtualQueryEx', 'DosPathToSessionPathA', 'GetApplicationRecoveryCallbackWorker', 'BaseCheckAppcompatCache', 'BackupSeek', 'CreateThreadpoolWork', 'SetWaitableTimer', 'CreateFile2', 'GetOEMCP', 'UnlockFileEx', 'CompareStringOrdinal', 'RtlUnwind', 'AllocateUserPhysicalPagesNuma', 'GetCurrentPackageInfo', 'GetWindowsDirectoryW', 'TermsrvSetValueKey', 'VDMConsoleOperation', 'SetFileValidData', 'GetWindowsDirectoryA', 'OpenProfileUserMapping', 'SetFileAttributesTransactedA', 'BackupWrite', 'VirtualProtectEx', 'CheckTokenCapability', 'GetThreadInformation', 'CloseProfileUserMapping', 'GetDiskSpaceInformationW', 'DisableThreadProfiling', 'CreateTimerQueueTimer', 'GetDiskSpaceInformationA', 'GetCurrencyFormatA', 'K32GetDeviceDriverFileNameW', 'CreateFileW', 'Wow64SetThreadContext', 'CreateFileA', 'K32GetDeviceDriverFileNameA', 'GetCurrencyFormatW', 'GetSystemWindowsDirectoryA', 'IsWow64Process2', 'GetCurrentThreadStackLimits', 'GetSystemWindowsDirectoryW', 'VirtualFree', 'OpenFile', 'Module32FirstW', 'PrivMoveFileIdentityW', 'LockResource', 'SetConsoleCursor', 'Basep8BitStringToDynamicUnicodeString', 'SetFileBandwidthReservation', 'GetPackageFullName', 'BasepCheckAppCompat', 'NotifyMountMgr', 'SetConsoleLocalEUDC', 'GetProcessDefaultCpuSets', 'GetCurrencyFormatEx', 'GetSystemAppDataKey', 'ReadDirectoryChangesExW', 'EnterSynchronizationBarrier', 'DeleteFiber', 'GetProcessDEPPolicy', 'SetConsoleCursorPosition', 'CheckForReadOnlyResource', 'GetApplicationUserModelId', 'IsValidLocaleName', 'K32GetModuleInformation', 'RtlUnwindEx', 'EnterUmsSchedulingMode', 'GetTapePosition', 'WaitCommEvent', 'IsValidNLSVersion', 'TransmitCommChar', 'PssWalkMarkerRewind', 'GetThreadTimes', 'GetConsoleHardwareState', 'SetComPlusPackageInstallStatus', 'EnumLanguageGroupLocalesW', 'ReadConsoleInputExW', 'CloseThreadpoolWork', 'GetStringTypeExW', 'EnumLanguageGroupLocalesA', 'GetStringTypeExA', 'ReadConsoleInputExA', 'SetLastError', 'BaseDestroyVDMEnvironment', 'GetWriteWatch', 'LoadEnclaveData', 'GetNumaProximityNodeEx', 'CreateHardLinkTransactedA', 'VerSetConditionMask', 'InitializeEnclave', 'EnumResourceTypesExA', 'CeipIsOptedIn', 'InvalidateConsoleDIBits', 'WritePrivateProfileSectionW', 'K32GetPerformanceInfo', 'EnumResourceTypesExW', 'WritePrivateProfileSectionA', 'SetThreadpoolThreadMinimum', 'DeleteBoundaryDescriptor', 'GetSystemFirmwareTable', 'FreeEnvironmentStringsA', 'TermsrvAppInstallMode', 'GetCurrentPackageFamilyName', 'SetThreadContext', 'BasepProcessInvalidImage', 'RegDeleteKeyExA', 'RegDeleteKeyExW', 'FindAtomA', 'CompareCalendarDates', 'LoadStringBaseW', 'GetCurrentThreadId', 'SetVolumeMountPointWStub', 'SetEvent', 'CheckAllowDecryptedRemoteDestinationPolicy', 'AcquireSRWLockShared', 'FlsSetValue', 'PssWalkMarkerSeek', 'IsNLSDefinedString', 'WerUnregisterExcludedMemoryBlock', 'ExitVDM', 'SetHandleInformation', 'GetFileSize', 'WriteFileGather', 'AddDllDirectory', 'GetProcAddress', 'GetCurrentProcessorNumber', 'EnumDateFormatsExA', 'HeapValidate', 'MapUserPhysicalPagesScatter', 'SleepConditionVariableCS', 'EnumDateFormatsExW', 'WriteProfileSectionA', 'ApplicationRecoveryFinished', 'DiscardVirtualMemory', 'WriteProfileSectionW', 'LocalUnlock', 'GetLongPathNameTransactedW', 'TrySubmitThreadpoolCallback', 'GetNamedPipeServerSessionId', 'PackageFamilyNameFromFullName', 'RtlDeleteFunctionTable', 'GetConsoleInputExeNameW', 'GetCommTimeouts', 'K32GetMappedFileNameW', '_lwrite', 'GetCompressedFileSizeW', 'K32GetMappedFileNameA', 'FindActCtxSectionStringWWorker', 'GetConsoleInputExeNameA', 'EnumTimeFormatsA', 'EnumDateFormatsExEx', 'IsCalendarLeapDay', 'GetCurrentActCtx', 'GetCompressedFileSizeA', 'TermsrvSetKeySecurity', 'SetFirmwareEnvironmentVariableA', 'ReadConsoleW', 'MapViewOfFile', 'GetModuleHandleA', 'DeleteVolumeMountPointW', 'GetUmsSystemThreadInformation', 'SetDllDirectoryA', 'FindPackagesByPackageFamily', 'Wow64RevertWow64FsRedirection', 'SetThreadToken', 'SetDllDirectoryW', 'SetLocalTime', 'GetModuleHandleW', 'BindIoCompletionCallback', 'GetCPInfoExW', 'ZombifyActCtxWorker', 'GetNumaProximityNode', 'BasepQueryModuleChpeSettings', 'CancelIoEx', 'SetProcessInformation', 'QueryFullProcessImageNameA', 'GetOverlappedResult', 'ScrollConsoleScreenBufferA', 'GetConsoleTitleW', 'SetThreadPriorityBoost', 'ScrollConsoleScreenBufferW', 'QueryFullProcessImageNameW', 'RegFlushKey', 'SetErrorMode', 'GetCalendarMonthsInYear', 'HeapWalk', 'GetCommModemStatus', 'ZombifyActCtx', 'GetProcessInformation', 'GetActiveProcessorGroupCount', 'GetConsoleTitleA', 'PssWalkMarkerGetPosition', 'GetSystemTimeAsFileTime', 'CreateThreadpoolIo', 'RaiseInvalid16BitExeError', 'GetThreadPriority', 'InterlockedPushListSListEx', 'Process32FirstW', 'GetCurrentPackageId', 'GetQueuedCompletionStatusEx', 'K32EnumProcessModules', 'IsThreadpoolTimerSet', 'Beep', 'PssWalkMarkerSeekToBeginning', 'SetConsoleScreenBufferSize', 'WaitForThreadpoolWaitCallbacks', 'EnumCalendarInfoA', 'SetFileShortNameW', 'GetFileMUIPath', 'WriteProfileStringA', 'UnregisterConsoleIME', 'InitializeConditionVariable', 'SetFileShortNameA', 'EnumCalendarInfoW', 'WriteProfileStringW', 'FindNextChangeNotification', 'GetNextVDMCommand', 'CreateSemaphoreA', 'K32EnumProcessModulesEx', 'EnumSystemLanguageGroupsA', 'CreateSemaphoreW', 'CtrlRoutine', 'EnumSystemLanguageGroupsW', 'ClearCommError', 'ExitThread', 'TerminateProcess', 'GetNumberFormatA', 'QueryUnbiasedInterruptTime', 'SetEndOfFile', 'GetNumberFormatW', 'LocalCompact', 'RegDeleteTreeW', 'RequestDeviceWakeup', 'TermsrvConvertSysRootToUserDir', 'CloseThreadpoolIo', 'GetExitCodeProcess', 'VirtualProtect', 'RegDeleteTreeA', 'BasepGetAppCompatData', 'RemoveDirectoryTransactedA', 'RemoveDirectoryTransactedW', 'ConvertThreadToFiberEx', 'GetApplicationRecoveryCallback', 'WaitNamedPipeW', 'WaitNamedPipeA', 'ConvertCalDateTimeToSystemTime', 'QuirkIsEnabled2Worker', 'SetVolumeLabelW', 'GetTimeZoneInformation', 'GetConsoleWindow', 'SetVolumeLabelA', 'SetProcessWorkingSetSizeEx', 'LeaveCriticalSection', 'FlushConsoleInputBuffer', 'CreateNamedPipeW', 'GetConsoleCP', 'RegisterApplicationRecoveryCallback', 'BaseFreeAppCompatDataForProcessWorker', 'CreateNamedPipeA', 'CreateThreadpool', 'SwitchToThread', 'GetTimeFormatEx', 'CreateIoCompletionPort', 'SetTapePosition', 'GetComPlusPackageInstallStatus', 'K32GetProcessMemoryInfo', 'WaitForThreadpoolIoCallbacks', 'Heap32ListNext', 'RegisterWaitForInputIdle', 'QuirkIsEnabledForPackage2Worker', 'BasepPostSuccessAppXExtension', 'RegLoadMUIStringW', 'UnregisterApplicationRestart', 'RegSetKeySecurity', 'RegLoadMUIStringA', 'GetHandleInformation', 'CloseThreadpoolCleanupGroupMembers', 'OpenFileMappingW', 'GetSystemDefaultLCID', 'IsCalendarLeapMonth', 'NtVdm64CreateProcessInternalW', 'IsDBCSLeadByteEx', 'FindResourceExA', 'ResolveLocaleName', 'SubmitThreadpoolWork', 'FindResourceExW', 'GetConsoleSelectionInfo', 'QueryActCtxWWorker', 'MoveFileA', 'UpdateCalendarDayOfWeek', 'GetSystemDefaultLocaleName', 'DeleteUmsThreadContext', 'SetConsoleWindowInfo', 'MoveFileW', 'CreateEnclave', 'FindFirstFileNameW', 'RegCreateKeyExW', 'ReadConsoleInputA', 'GetUserDefaultLangID', 'FindNextVolumeA', 'FindFirstFileTransactedA', 'ReadConsoleInputW', 'RegCreateKeyExA', 'BaseDumpAppcompatCache', 'FindNextVolumeW', 'ExpungeConsoleCommandHistoryA', 'ExpungeConsoleCommandHistoryW', 'LoadStringBaseExW', 'InterlockedFlushSList', 'GetSystemDirectoryW', 'BasepCheckWinSaferRestrictions', 'BasepGetComputerNameFromNtPath', 'GetSystemDirectoryA', 'SetSystemTime', 'AllocateUserPhysicalPages', 'GetModuleHandleExW', 'LocalFileTimeToFileTime', 'GetModuleHandleExA', 'FindFirstFileTransactedW', 'GetConsoleKeyboardLayoutNameW', 'GetConsoleKeyboardLayoutNameA', 'GlobalSize', 'DosDateTimeToFileTime', 'ReclaimVirtualMemory', 'GetStagedPackagePathByFullName', 'DeleteFileA', 'DeleteFileW', 'CreateWaitableTimerW', 'AssignProcessToJobObject', 'CreateWaitableTimerExW', 'ExpandEnvironmentStringsW', 'GetNamedPipeServerProcessId', 'GetThreadDescription', 'CreateWaitableTimerExA', 'RtlLookupFunctionEntry', 'CreateWaitableTimerA', 'TermsrvGetPreSetValue', 'LZCloseFile', 'ExpandEnvironmentStringsA', 'LocalSize', 'WerUnregisterFile', 'PackageNameAndPublisherIdFromFamilyName', 'SetVDMCurrentDirectories', 'GlobalGetAtomNameW', 'GetSystemInfo', 'GlobalGetAtomNameA', 'GlobalUnlock', 'LCIDToLocaleName', 'GetAtomNameA', 'GlobalAddAtomExW', 'FreeMemoryJobObject', 'GlobalAddAtomExA', 'GetAtomNameW', 'VDMOperationStarted', 'SetThreadAffinityMask', 'GetTickCount64', 'NlsUpdateLocale', 'ReadConsoleOutputCharacterW', 'ReadConsoleOutputCharacterA', 'GetProcessWorkingSetSizeEx', 'SetThreadUILanguage', 'IsBadHugeWritePtr', 'CreateProcessA', '_hwrite', 'GetNumaHighestNodeNumber', 'HeapCreate', 'GetDefaultCommConfigW', 'CreateProcessW', 'GetDefaultCommConfigA', 'IsEnclaveTypeSupported', 'CreateFiberEx', 'VerifyVersionInfoA', 'FileTimeToSystemTime', 'GetConsoleCommandHistoryW', 'RemoveSecureMemoryCacheCallback', 'ContinueDebugEvent', 'GetConsoleCommandHistoryA', 'VerifyVersionInfoW', 'K32InitializeProcessForWsWatch', 'RtlRaiseException', 'WriteConsoleOutputW', 'VirtualLock', 'PrefetchVirtualMemory', 'CommConfigDialogA', 'GetFileAttributesTransactedW', 'CheckElevationEnabled', 'IsSystemResumeAutomatic', 'WerpGetDebugger', 'GetFileAttributesTransactedA', 'K32QueryWorkingSetEx', 'ReleaseActCtx', 'WerRegisterFileWorker', 'WerpNotifyLoadStringResourceWorker', 'SetThreadSelectedCpuSets', 'FreeLibrary', 'LocalFree', 'PssWalkMarkerCreate', 'GetProcessorSystemCycleTime', 'MapViewOfFileExNuma', 'IsNativeVhdBoot', 'OpenThread', 'CopyFileW', 'lstrcpynW', 'ClosePseudoConsole', 'GetModuleFileNameW', 'CopyFileA', 'GetModuleFileNameA', 'SetConsoleOutputCP', 'CreateFileMappingFromApp', 'SetConsoleFont', 'BaseCheckAppcompatCacheExWorker', 'CopyLZFile', 'BasepGetExeArchType', 'GetStateFolder', 'BasepCopyEncryption', 'BasepFreeActivationContextActivationBlock', 'SetConsoleIcon', 'GetUserDefaultLocaleName', 'CopyFile2', 'GlobalAlloc', 'GetFileBandwidthReservation', 'K32QueryWorkingSet', 'InitializeCriticalSectionAndSpinCount', 'TermsrvDeleteValue', 'PssQuerySnapshot', 'WerUnregisterAppLocalDump', 'PssWalkSnapshot', 'lstrcpynA', 'CreateMailslotW', 'LZSeek', 'SetProtectedPolicy', 'SetConsoleTextAttribute', 'CreateMailslotA', 'FindFirstFileNameTransactedW', 'BaseCheckAppcompatCacheWorker', 'SetCommMask', 'SetFileInformationByHandle', 'SetSystemTimeAdjustment', 'GetNumberOfConsoleFonts', 'GlobalFix', 'ResetEvent', 'GetActiveProcessorCount', 'IsValidLanguageGroup', 'Wow64GetThreadSelectorEntry', 'GetThreadErrorMode', 'TlsSetValue', 'LocalReAlloc', 'CreateFileMappingW', 'BaseCleanupAppcompatCacheSupport', 'SetThreadPreferredUILanguages', 'CancelWaitableTimer', 'AddConsoleAliasA', 'GetCurrentProcessId', 'GetProcessHeaps', 'AddConsoleAliasW', 'uaw_wcscpy', 'RemoveVectoredContinueHandler', 'WerpNotifyUseStringResourceWorker', 'QueryThreadCycleTime', 'RegQueryInfoKeyW', 'SetFilePointer', 'ReadFile', 'RtlCaptureContext', 'WerUnregisterAdditionalProcess', 'RegQueryInfoKeyA', 'IsBadStringPtrW', 'RegDisablePredefinedCacheEx', 'SetConsoleMode', 'SetConsolePalette', 'SetConsoleDisplayMode', 'OpenConsoleWStub', 'IsBadStringPtrA', 'GetTimeFormatAWorker', 'QuirkIsEnabledForPackageWorker', 'GetFileAttributesA', 'EncodePointer', 'GetUserDefaultGeoName', 'GetFileAttributesW', 'GetLocalTime', 'SetNamedPipeAttribute', 'K32EnumDeviceDrivers', 'UnhandledExceptionFilter', '_llseek', 'GetFileInformationByHandle', 'GetGeoInfoEx', 'WriteConsoleOutputAttribute', 'WriteConsoleOutputA', 'QueryIoRateControlInformationJobObject', 'GetProfileIntW', 'GetPackageInfo', 'AppPolicyGetLifecycleManagement', 'GetProfileIntA', 'GetStringScripts', 'RegNotifyChangeKeyValue', 'ShowConsoleCursor', 'TermsrvDeleteKey', 'ActivateActCtx', 'GetErrorMode', 'GetDiskFreeSpaceExA', 'RegSetValueExW', 'ConvertThreadToFiber', 'GetProcessShutdownParameters', 'SetCurrentDirectoryW', 'RegSetValueExA', 'GetDiskFreeSpaceExW', 'GetSystemPreferredUILanguages', 'SetCurrentDirectoryA', 'PowerSetRequest', 'RegCloseKey', 'PssWalkMarkerTell', 'SetThreadStackGuarantee', 'SetVolumeMountPointA', 'SetupComm', 'GetSystemRegistryQuota', 'SetVolumeMountPointW', 'GetComputerNameW', 'SetDefaultDllDirectories', 'lstrcmpA', 'FindNextFileW', 'QuirkIsEnabledForPackage4Worker', 'WerGetFlags', 'GetConsoleScreenBufferInfoEx', 'GetComputerNameA', 'FindNextFileA', 'lstrcmpW', 'EscapeCommFunction', 'CreateEventExW', 'RegEnumValueW', 'lstrcmpi', 'RegEnumValueA', 'GetApplicationRestartSettings', 'CreateEventExA', 'ReplacePartitionUnit', 'RegOpenCurrentUser', 'WerRegisterRuntimeExceptionModule', 'BaseVerifyUnicodeString', 'CloseThreadpoolTimer', 'SetThreadpoolStackInformation', 'CloseThreadpoolCleanupGroup', 'Wow64DisableWow64FsRedirection', 'CancelThreadpoolIo', 'GetCommandLineW', 'QuirkIsEnabled3Worker', 'GetEnabledXStateFeatures', 'FlsAlloc', 'GetCommandLineA', 'DecodeSystemPointer', 'CreateThreadpoolTimer', 'FindNextFileNameW', 'BaseInitAppcompatCacheSupportWorker', 'SetStdHandleEx', 'AppPolicyGetClrCompat', 'timeGetDevCaps', 'PssCaptureSnapshot', 'PackageFamilyNameFromId', 'GetConsoleAliasExesLengthA', 'WerRegisterExcludedMemoryBlock', 'BaseFlushAppcompatCacheWorker', 'GetConsoleAliasExesLengthW', 'GetProcessVersion', 'FlsGetValue', 'SystemTimeToTzSpecificLocalTime', 'GetProcessId', 'SetDefaultCommConfigW', 'DeleteCriticalSection', 'RtlZeroMemory', 'SetDefaultCommConfigA', 'GetFileTime', 'WideCharToMultiByte', 'SetTapeParameters', 'Thread32First', 'BasepFreeAppCompatData', 'K32GetWsChanges', 'BaseDumpAppcompatCacheWorker', 'GlobalFindAtomW', 'HeapFree', 'BaseCheckAppcompatCacheEx', 'GetSystemFileCacheSize', 'GlobalCompact', 'GlobalFindAtomA', 'RtlAddFunctionTable', 'FatalExit', 'SetProcessDEPPolicy', 'WerRegisterMemoryBlock', 'CreateActCtxW', 'Heap32First', 'GetProfileSectionW', 'CreateActCtxA', 'GetProfileSectionA', 'TermsrvCreateRegEntry', 'GetThreadIdealProcessorEx', 'ConvertDefaultLocale', 'GetNumberOfConsoleMouseButtons', 'GetCurrentUmsThread', 'ResolveDelayLoadedAPI', 'GlobalUnWire', 'EnumSystemLocalesEx', 'SetEnvironmentStringsA', 'LoadLibraryW', 'GetPrivateProfileIntA', 'DuplicateEncryptionInfoFileExt', 'AdjustCalendarDate', 'LoadLibraryA', 'SetEnvironmentStringsW', 'GetConsoleCommandHistoryLengthA', 'UnregisterBadMemoryNotification', 'ReadProcessMemory', 'GetConsoleScreenBufferInfo', 'FillConsoleOutputAttribute', 'GetConsoleCommandHistoryLengthW', 'K32GetWsChangesEx', 'DeleteFileTransactedA', 'uaw_lstrcmpW', 'SetThreadpoolTimer', 'LZCopy', 'DeleteFileTransactedW', 'GetProcessWorkingSetSize', 'DuplicateHandle', 'RtlInstallFunctionTableCallback', 'AddScopedPolicyIDAce', 'GetNamedPipeClientSessionId', 'GetPrivateProfileIntW', 'GetOverlappedResultEx', 'GetProcessHandleCount', 'ConsoleMenuControl', 'SetFileCompletionNotificationModes', 'GetPackagePathByFullName', 'SetConsoleMenuClose', 'SetProcessAffinityUpdateMode', 'BaseInitAppcompatCacheSupport', 'NlsUpdateSystemLocale', 'TryAcquireSRWLockShared', 'SleepConditionVariableSRW', 'QueryPerformanceFrequency', 'SetUserGeoID', 'GetConsoleCursorMode', 'DeactivateActCtxWorker', 'BasepCheckWebBladeHashes', 'CreateRemoteThreadEx', 'GetSystemTimeAdjustment', 'GetLogicalProcessorInformation', 'ConvertSystemTimeToCalDateTime', 'RtlMoveMemory', 'InitializeSynchronizationBarrier', 'AppXGetOSMaxVersionTested', 'GetStdHandle', 'InitOnceInitialize', 'AddIntegrityLabelToBoundaryDescriptor', 'CreateTapePartition', 'IsCalendarLeapYear', 'StartThreadpoolIo', 'InstallELAMCertificateInfo', 'ReadFileScatter', 'FindNextVolumeMountPointA', 'FindFirstStreamW', 'FindNextVolumeMountPointW', 'Module32NextW', 'GetCPInfoExA', 'SetFileAttributesA', 'PackageFullNameFromId', 'CheckForReadOnlyResourceFilter', 'GetExpandedNameW', 'GetFirmwareType', 'AllocConsole', 'SetFileAttributesW', 'CloseConsoleHandle', 'GetExpandedNameA', 'PeekNamedPipe', 'GetLargestConsoleWindowSize', 'WakeConditionVariable', 'LoadLibraryExA', 'BaseUpdateAppcompatCacheWorker', 'LoadLibraryExW', 'OpenConsoleW', 'BaseSetLastNTError', 'SetThreadInformation', 'LZRead', 'IsProcessorFeaturePresent', 'GetMaximumProcessorCount', 'ReadConsoleA', 'NotifyUILanguageChange', 'K32GetDeviceDriverBaseNameA', 'PssFreeSnapshot', 'WerRegisterMemoryBlockWorker', '_lcreat', 'LocalFileTimeToLocalSystemTime', 'SetThreadGroupAffinity', 'GetNumberFormatEx', 'K32GetDeviceDriverBaseNameW', 'CreateToolhelp32Snapshot', 'GetNumaProcessorNodeEx', 'CopyContext', 'GetConsoleFontSize', 'WriteConsoleInputA', 'LZDone', 'TlsAlloc', 'WriteConsoleInputW', 'lstrcat', 'OpenProcessToken', 'OpenFileMappingA', 'AcquireSRWLockExclusive', 'AddAtomA', 'RegisterWaitUntilOOBECompleted', 'timeEndPeriod', 'FindActCtxSectionGuid', 'WaitForMultipleObjects', 'AddAtomW', 'IdnToNameprepUnicode', 'SetThreadpoolWaitEx', 'PssWalkMarkerFree', 'RtlCopyMemory', 'IdnToAscii', 'GetLocaleInfoEx', 'GetNLSVersion', 'UpdateProcThreadAttribute', 'SetMessageWaitingIndicator', 'SetProcessShutdownParameters', 'GetConsoleAliasesLengthA', 'GetConsoleAliasesLengthW', 'NlsGetCacheUpdateCount', 'WaitForSingleObjectEx', 'GetCalendarInfoEx', 'CheckRemoteDebuggerPresent', 'CompareFileTime', 'PowerClearRequest', 'SetConsoleCursorInfo', 'FlsFree', 'GetCurrentThread', 'RegisterWaitForSingleObjectEx', 'RaiseException', 'ReleaseSemaphore', 'SystemTimeToTzSpecificLocalTimeEx', 'SetSystemPowerState', 'UTUnRegister', 'BasepInitAppCompatData', 'DeleteProcThreadAttributeList', 'WerUnregisterRuntimeExceptionModuleWorker', 'UnmapViewOfFileEx', 'LZClose', 'GetUserPreferredUILanguages', 'K32GetProcessImageFileNameW', 'K32GetProcessImageFileNameA', 'GetCurrentProcess', 'MapViewOfFileEx', 'NlsWriteEtwEvent', 'HeapSize', 'FlushProcessWriteBuffers', 'SetConsoleCP', 'FormatMessageW', 'WerUnregisterCustomMetadata', 'FormatMessageA', 'GetConsoleFontInfo', 'QueryProcessCycleTime', 'RegisterConsoleVDM', 'GetMemoryErrorHandlingCapabilities', 'GetNamedPipeInfo', 'InitOnceComplete', 'SetConsoleTitleW', 'DnsHostnameToComputerNameExW', 'OpenWaitableTimerA', 'CancelDeviceWakeupRequest', 'RtlVirtualUnwind', 'CheckTokenMembershipEx', 'OpenWaitableTimerW', 'FlushInstructionCache', 'AppPolicyGetProcessTerminationMethod', 'SetUnhandledExceptionFilter', 'GetDateFormatAWorker', 'MulDiv', 'UnlockFile', 'RegisterWowBaseHandlers', 'ReleaseSRWLockShared', 'RegSaveKeyExA', 'RegSaveKeyExW', 'FindFirstStreamTransactedW', 'BaseThreadInitThunk', 'GetVersion', 'RaiseFailFastException', 'BaseWriteErrorElevationRequiredEvent', 'uaw_lstrcmpiW', 'SetHandleCount', 'lstrcmp', 'GetTickCount', 'SetLocalPrimaryComputerNameA', 'BaseUpdateVDMEntry', 'RegisterApplicationRestart', 'SetLocalPrimaryComputerNameW', 'FindStringOrdinal', 'lstrcpyW', 'AddSecureMemoryCacheCallback', 'AddSIDToBoundaryDescriptor', '_hread', 'CheckElevation', 'lstrcpyA', 'GetTempFileNameA', 'Thread32Next', 'SetCommTimeouts', 'WerRegisterFile', 'SetProcessPreferredUILanguages', 'PrepareTape', 'lstrcpyn', 'GetTempFileNameW', 'TerminateJobObject', 'GetLogicalProcessorInformationEx', 'lstrlenA', 'GetEnvironmentStringsA', 'GetProcessTimes', 'GetEnvironmentStringsW', 'IsDBCSLeadByte', 'GetConsoleHistoryInfo', 'lstrlenW', 'WinExec', 'UnregisterWait', 'GetFileSizeEx', 'GetCalendarDifferenceInDays', 'BaseIsAppcompatInfrastructureDisabled', 'GetCalendarWeekNumber', 'CancelIo', 'InitializeContext2', 'SortCloseHandle', 'PeekConsoleInputW', 'PulseEvent', 'FindActCtxSectionGuidWorker', 'PeekConsoleInputA', 'GetCommConfig', 'GetConsoleInputWaitHandle', 'IsValidCodePage', 'UnmapViewOfFile', 'SetThreadLocale', 'GetConsoleOutputCP', 'GetPrivateProfileStructA', 'WerSetFlags', 'DeleteAtom', 'GetCurrentPackagePath', 'LZInit', 'Wow64SuspendThread', 'CreateTimerQueue', 'QueueUserAPC', 'GetDurationFormat', 'GetPrivateProfileStructW', 'CreateSymbolicLinkTransactedA', 'LocalAlloc', 'CreateSymbolicLinkTransactedW', 'RequestWakeupLatency', 'CreateUmsThreadContext', 'GetStringTypeA', 'GetDiskFreeSpaceW', 'WerSetFlagsWorker', 'GetNumaNodeProcessorMaskEx', 'SwitchToFiber', 'SetThreadDescription', 'GetDiskFreeSpaceA', 'GetStringTypeW', 'HeapLock', 'ConnectNamedPipe', 'GetEnvironmentVariableA', '__chkstk', 'EnumResourceNamesExA', 'FindClose', 'EnumResourceNamesExW', 'GetEnvironmentVariableW', 'DeviceIoControl', 'HeapSummary', 'DeleteTimerQueueEx', 'OpenState', 'FoldStringA', 'EnumSystemLocalesA', 'LockFileEx', 'SetThreadPriority', 'EnumSystemLocalesW', 'UnregisterWaitUntilOOBECompleted', 'FoldStringW', 'SetProcessAffinityMask', 'SetCalendarInfoA', 'RtlCaptureStackBackTrace', 'InterlockedPushListSList', 'SetCalendarInfoW', 'SetLastConsoleEventActive', 'GetDynamicTimeZoneInformation', 'InitOnceBeginInitialize', 'BasepReportFault', 'GetThreadSelectorEntry', 'AddLocalAlternateComputerNameW', 'AddLocalAlternateComputerNameA', 'GetPackageFamilyName', 'AddRefActCtx', 'FreeLibraryWhenCallbackReturns', 'QueryThreadProfiling', 'GetVersionExW', 'IsBadWritePtr', 'GetVersionExA', 'Process32First', '_lread', 'AppPolicyGetThreadInitializationType', 'FindFirstFileA', 'WerGetFlagsWorker', 'FindFirstFileW', 'IsValidLocale', 'SetConsoleHardwareState', 'CreateEventW', 'OpenJobObjectW', 'UTRegister', 'OpenPackageInfoByFullName', 'CreateEventA', 'OpenJobObjectA', 'LCMapStringW', 'GetCurrentPackageFullName', 'LCMapStringA', 'GetThreadLocale', 'WerRegisterCustomMetadata', 'GetNumaNodeProcessorMask', 'GetQueuedCompletionStatus', 'SetComputerNameEx2W', 'GetEnvironmentStrings', 'SetConsoleKeyShortcuts', 'CloseThreadpool', 'CopyFileExA', 'GetSystemDEPPolicy', 'GetEncryptedFileVersionExt', 'OpenMutexA', 'TlsFree', 'CreateSymbolicLinkW', 'GlobalFlags', 'PrivCopyFileExW', 'OpenMutexW', 'OOBEComplete', 'CreateSymbolicLinkA', 'GetFileAttributesExW', 'ReadFileEx', 'uaw_wcschr', 'LocalShrink', 'BaseElevationPostProcessing', 'LocalSystemTimeToLocalFileTime', 'ReplaceFileA', 'Toolhelp32ReadProcessMemory', 'ConvertNLSDayOfWeekToWin32DayOfWeek', 'lstrlen', 'ReplaceFileW', 'GetBinaryType', 'GetVolumePathNamesForVolumeNameW', 'HeapQueryInformation', 'AppPolicyGetMediaFoundationCodecLoading', 'Heap32Next', 'GetLocaleInfoA', 'GetVolumePathNamesForVolumeNameA', 'FreeEnvironmentStringsW', 'GetLocaleInfoW', 'RestoreLastError', 'SetStdHandle', 'BaseFlushAppcompatCache', 'SetThreadIdealProcessorEx', 'WaitForDebugEvent', 'SetComputerNameW', 'OpenThreadToken', '_lopen', 'SetComputerNameA', 'ExecuteUmsThread', 'ResumeThread', 'GetThreadSelectedCpuSets', 'FreeLibraryAndExitThread', 'EnumSystemGeoID', 'BaseCleanupAppcompatCacheSupportWorker', 'VerLanguageNameA', 'GetUmsCompletionListEvent', 'GetCachedSigningLevel', 'VerLanguageNameW', 'SetProcessMitigationPolicy', 'FatalAppExitW', 'GetVolumeInformationA', 'GetVolumeInformationW', 'FatalAppExitA', 'GetSystemPowerStatus', 'GetVolumeNameForVolumeMountPointA', 'EraseTape', 'K32EnumProcesses', 'GetSystemDefaultUILanguage', 'GetProcessPriorityBoost', 'QuirkIsEnabledForPackage3Worker', 'GetVolumeNameForVolumeMountPointW', 'WaitForMultipleObjectsEx', 'FindCloseChangeNotification', 'InitializeSRWLock', 'GetSystemWow64DirectoryW', 'SetCommBreak', 'LZOpenFileA', 'QueryPerformanceCounter', 'GetSystemWow64DirectoryA', 'GetCommMask', 'LZOpenFileW', 'GlobalUnfix', 'GetFileMUIInfo', 'ConvertFiberToThread', 'LoadModule', 'GetFileAttributesExA', 'GetXStateFeaturesMask', 'QueryDepthSList', 'GetProfileStringW', 'GetTimeFormatWWorker', 'GetPackagesByPackageFamily', 'GetProfileStringA', 'CreateFileMappingA', 'MapViewOfFileFromApp', 'GetPrivateProfileSectionW', 'SetConsoleInputExeNameW', 'AddResourceAttributeAce', 'SetConsoleInputExeNameA', 'GetPrivateProfileSectionA', 'BuildCommDCBA', 'GetLastError', 'GetShortPathNameW', 'GetDurationFormatEx', 'GetConsoleAliasExesA', 'BuildCommDCBW', 'GetConsoleAliasExesW', 'GetShortPathNameA', '__misaligned_access', 'SetProcessDefaultCpuSets', 'BaseIsDosApplication', 'GetProcessPreferredUILanguages', 'LocaleNameToLCID', 'SuspendThread', 'GetSystemDefaultLangID', 'SetCurrentConsoleFontEx', 'RegEnumKeyExW', 'SetConsoleCursorMode', 'SetProcessWorkingSetSize', 'CloseHandle', 'CreatePseudoConsole', 'FreeResource', 'SetCommConfig', 'GetThreadId', 'IsNormalizedString', 'OpenEventW', 'WerRegisterAdditionalProcess', 'IsBadReadPtr', 'InitializeContext', 'OpenEventA', 'BaseIsAppcompatInfrastructureDisabledWorker', 'RegRestoreKeyA', 'GetPrivateProfileSectionNamesA', 'GetDriveTypeW', 'GetDriveTypeA', 'FindNextStreamW', 'GetPrivateProfileSectionNamesW', 'RegRestoreKeyW', 'SetInformationJobObject', 'ActivateActCtxWorker', 'GetTapeParameters', 'RegEnumKeyExA', 'GetFirmwareEnvironmentVariableExA', 'CloseThreadpoolWait', 'GetNumaAvailableMemoryNodeEx', 'InitializeSListHead', 'GetFirmwareEnvironmentVariableExW', 'CreatePrivateNamespaceW', 'GetTempPathA', 'GetCPInfo', 'GetThreadIOPendingFlag', 'GetTempPathW', 'CreatePrivateNamespaceA', 'EnumDateFormatsW', 'OutputDebugStringW', 'EnumDateFormatsA', 'BasepSetFileEncryptionCompression', 'OutputDebugStringA', 'WerUnregisterMemoryBlock', 'ReadDirectoryChangesW', 'GetUserDefaultUILanguage', 'WriteProcessMemory', 'RegQueryValueExA', 'DequeueUmsCompletionListItems', 'TryEnterCriticalSection', 'GetProcessGroupAffinity', 'HeapAlloc', 'uaw_wcsrchr', 'FlushViewOfFile', 'RegQueryValueExW', 'GetVolumeInformationByHandleW', 'WerpLaunchAeDebug', 'SetThreadErrorMode', 'InitializeProcThreadAttributeList', 'NormalizeString', 'GlobalAddAtomW', 'SetEnvironmentVariableW', 'SetNamedPipeHandleState', 'GlobalAddAtomA', 'GetMailslotInfo', 'SetEnvironmentVariableA', 'SetPriorityClass', 'GetCommState', 'LZStart', 'ChangeTimerQueueTimer', 'LCMapStringEx', 'RtlCompareMemory', 'lstrcatA', 'FillConsoleOutputCharacterA', 'GetConsoleCursorInfo', 'FillConsoleOutputCharacterW', 'CreateRemoteThread', 'BaseDllReadWriteIniFile', 'OpenFileById', 'GetCommProperties', 'SetTermsrvAppInstallMode', 'CompareStringW', 'GetDllDirectoryW', '_local_unwind', 'GetDllDirectoryA', 'CompareStringA', 'InitOnceExecuteOnce', 'CreateUmsCompletionList', 'lstrcatW', 'LoadPackagedLibrary', 'SetFileApisToOEM', 'BasepMapModuleHandle', 'GetDateFormatEx', 'ReadConsoleOutputAttribute', 'SystemTimeToFileTime', 'QueryIdleProcessorCycleTimeEx', 'BaseReadAppCompatDataForProcessWorker', 'CloseState', 'EnumerateLocalComputerNamesA', 'GetCurrentDirectoryW', 'VirtualFreeEx', 'GetMaximumProcessorGroupCount', 'ProcessIdToSessionId', 'GetCurrentDirectoryA', 'GetConsoleCharType', 'EnumerateLocalComputerNamesW', 'BackupRead', 'EnumCalendarInfoExW', 'WerRegisterAppLocalDump', 'WritePrivateProfileStringW', 'EnumSystemCodePagesW', 'WriteTapemark', 'EnumSystemCodePagesA', 'CreateConsoleScreenBuffer', 'SetThreadExecutionState', 'RegUnLoadKeyA', 'WerpInitiateRemoteRecovery', 'WriteFile', 'BaseGenerateAppCompatData', 'RegUnLoadKeyW', 'WritePrivateProfileStringA', 'CreateJobObjectA', 'FileTimeToDosDateTime', 'SetConsoleMaximumWindowSize', 'GetConsoleAliasW', 'CreateJobObjectW', 'GetEraNameCountedString', 'GetPackageApplicationIds', 'EnumCalendarInfoExA', 'IsProcessInJob', 'QuirkGetDataWorker', 'FindActCtxSectionStringA', 'lstrcpy', 'CreateActCtxWWorker', 'FindActCtxSectionStringW', 'QueryProtectedPolicy', 'LoadResource', 'FindFirstVolumeMountPointW', 'SetConsoleHistoryInfo', 'DeleteTimerQueue', 'DeleteUmsCompletionList', 'FindFirstVolumeMountPointA', 'SetThreadpoolTimerEx', 'VerifyConsoleIoHandle', 'ApplicationRecoveryInProgress', 'AddVectoredExceptionHandler', 'GetNumberOfConsoleInputEvents', 'ExitProcess', 'SetConsoleNlsMode', 'DeleteSynchronizationBarrier', 'CreateDirectoryTransactedW', 'CreateDirectoryTransactedA', 'ParseApplicationUserModelId', 'ClosePackageInfo', 'RegisterWaitForSingleObject', '_lclose', 'SetSystemFileCacheSize', 'CopyFileTransactedW', 'LocalFlags', 'GetConsoleDisplayMode', 'SetThreadIdealProcessor', 'WriteFileEx', 'TzSpecificLocalTimeToSystemTime', 'CopyFileTransactedA', 'ReadConsoleOutputW', 'GetCompressedFileSizeTransactedA', 'GetCompressedFileSizeTransactedW', 'SetXStateFeaturesMask', 'ReadConsoleOutputA', 'CallNamedPipeW', 'CreateHardLinkTransactedW', 'BasepReleaseSxsCreateProcessUtilityStruct', 'EnterCriticalSection', 'ReOpenFile', 'lstrcmpiA', 'FindVolumeClose', 'CallNamedPipeA', 'MoveFileWithProgressA', 'lstrcmpiW', 'IsThreadAFiber', 'GetDateFormatA', 'CreateDirectoryA', 'WerUnregisterMemoryBlockWorker', 'GetDateFormatW', 'GenerateConsoleCtrlEvent', 'CreateDirectoryW', 'GetUserDefaultLCID', 'GetNumaNodeNumberFromHandle', 'GetComputerNameExA', 'GetTimeFormatW', 'GlobalWire', 'GlobalReAlloc', 'EnumTimeFormatsEx', 'QueryActCtxSettingsWWorker', 'WTSGetActiveConsoleSessionId', 'CreateMemoryResourceNotification', 'GetTimeFormatA', 'GetComputerNameExW', 'SetWaitableTimerEx', 'BaseGetNamedObjectDirectory', 'IsWow64GuestMachineSupported', 'DuplicateConsoleHandle', 'CreateProcessInternalA', 'GetNLSVersionEx', 'CreateProcessInternalW', 'PackageIdFromFullName', 'GetNativeSystemInfo', 'DefineDosDeviceW', 'Heap32ListFirst', 'FindFirstChangeNotificationA', 'GlobalFree', 'CreateThreadpoolCleanupGroup', 'DefineDosDeviceA', 'GetThreadUILanguage', 'GetUserGeoID', 'FindFirstChangeNotificationW', 'BaseFormatTimeOut', 'PssWalkMarkerSetPosition', 'BaseFormatObjectAttributes', 'GetFinalPathNameByHandleW', 'CreateFileMappingNumaW', 'CreateFileMappingNumaA', 'GetFinalPathNameByHandleA', 'OpenStateExplicit', 'GetGeoInfoA', 'NlsEventDataDescCreate', 'CreateFileTransactedA', 'WaitForDebugEventEx', 'GetGeoInfoW', 'SetUserGeoName', 'OpenSemaphoreA', 'LocalHandle', 'OpenSemaphoreW', 'RegOpenUserClassesRoot', 'EnumUILanguagesA', 'GetLargePageMinimum', 'LoadAppInitDlls', 'EnableThreadProfiling', 'RegisterBadMemoryNotification', 'PurgeComm', 'DebugBreak', 'EnumUILanguagesW', 'GetProcessMitigationPolicy', 'BasepAnsiStringToDynamicUnicodeString', 'GetPackagePath', 'CreatePipe', 'FindFirstFileExW', 'GetConsoleAliasA', 'DebugActiveProcessStop', 'RegOpenKeyExW', 'CmdBatNotification', 'GetConsoleProcessList', 'RegOpenKeyExA', 'GetCalendarDateFormatEx', 'SetTimerQueueTimer', 'AppPolicyGetCreateFileAccess', 'SetConsoleScreenBufferInfoEx', 'IsBadHugeReadPtr', 'GlobalMemoryStatusEx', 'HeapReAlloc', 'TermsrvOpenRegEntry', 'IsWow64Process', 'InitAtomTable', 'BeginUpdateResourceW', 'GetApplicationRestartSettingsWorker', 'HeapDestroy', 'BeginUpdateResourceA', 'LocalLock', 'UpdateResourceW', 'timeBeginPeriod', 'UpdateResourceA', 'SetConsoleCtrlHandler', 'GetDateFormatWWorker', 'SortGetHandle', 'DelayLoadFailureHook', 'Module32First', 'DeleteVolumeMountPointA', 'CreateThread', 'GetExitCodeThread', 'Module32Next', 'GetSystemTimes', 'RegDeleteValueW', 'RemoveLocalAlternateComputerNameA', 'WriteConsoleA', 'RtlFillMemory', 'GetConsoleOriginalTitleA', 'VirtualQuery', 'DebugActiveProcess', 'CommConfigDialogW', 'GetVDMCurrentDirectories', 'RegDeleteValueA', 'GetConsoleOriginalTitleW', 'SleepEx', 'WriteConsoleW', 'SetThreadpoolWait', 'EndUpdateResourceW', 'GetCurrentConsoleFontEx', 'SetUmsThreadInformation', 'InitializeCriticalSectionEx', 'EndUpdateResourceA', 'Process32Next', 'GetStartupInfoA', 'GetProcessIoCounters', '__C_specific_handler', 'RtlPcToFileHeader', 'BasepAppXExtension', 'WakeAllConditionVariable', 'GetNamedPipeHandleStateA', 'BasepQueryAppCompat', 'GetStartupInfoW', 'FindVolumeMountPointClose', 'GetNamedPipeHandleStateW', 'CreateHardLinkA', 'PssDuplicateSnapshot', 'DebugBreakProcess', 'LocateXStateFeature', 'CreateHardLinkW', 'FindAtomW', 'GetProcessIdOfThread', 'RemoveDllDirectory', 'EncodeSystemPointer', 'timeGetSystemTime', 'GetFileType', 'RemoveVectoredExceptionHandler', 'AttachConsole', 'GetCurrentActCtxWorker', 'GlobalDeleteAtom', 'SetConsoleNumberOfCommandsA', 'SetThreadpoolThreadMaximum', 'GetDevicePowerState', 'SetConsoleNumberOfCommandsW', 'AppPolicyGetWindowingModel', 'CreateFiber', 'FileTimeToLocalFileTime', 'SizeofResource', 'BuildCommDCBAndTimeoutsA', 'BuildCommDCBAndTimeoutsW', 'QueryActCtxW', 'SetFirmwareEnvironmentVariableW', 'GetCalendarSupportedDateRange', 'GetAppContainerAce', 'SetConsoleTitleA', 'SetSearchPathMode', 'GetPhysicallyInstalledSystemMemory', 'OfferVirtualMemory', 'SetComputerNameExA', 'NlsCheckPolicy', 'PostQueuedCompletionStatus', 'UnregisterApplicationRecoveryCallback', 'GetAppContainerNamedObjectPath', 'SetComputerNameExW', 'GetSystemCpuSetInformation', 'WerUnregisterRuntimeExceptionModule', 'EnumSystemFirmwareTables', 'SetIoRateControlInformationJobObject', 'RegisterConsoleOS2', 'FormatApplicationUserModelId', 'GetNamedPipeClientComputerNameA', 'GetNamedPipeClientComputerNameW', 'LZCreateFileW', 'IsProcessCritical', 'QueryMemoryResourceNotification', 'ResolveDelayLoadsFromDll', 'WritePrivateProfileStructA', 'WritePrivateProfileStructW', 'BasepIsProcessAllowed', 'GetFullPathNameA', 'QueryDosDeviceA', 'RemoveLocalAlternateComputerNameW', 'InitializeCriticalSection', 'SetLocaleInfoA', 'GlobalHandle', 'uaw_lstrlenW', 'QueryDosDeviceW', 'GetFullPathNameW', 'QueueUserWorkItem', 'SetLocaleInfoW', 'CancelTimerQueueTimer', 'ReplaceFile', 'FindNLSString', 'BasepNotifyLoadStringResource', 'CreateBoundaryDescriptorW', 'HeapSetInformation', 'GetPriorityClass', 'GetPrivateProfileStringA', 'AppPolicyGetShowDeveloperDiagnostic', 'TermsrvSyncUserIniFileExt', 'CreateBoundaryDescriptorA', 'GetPrivateProfileStringW', 'K32GetModuleBaseNameA', 'GetFirmwareEnvironmentVariableW', 'CreateDirectoryExW', 'DebugSetProcessKillOnExit', 'GetFirmwareEnvironmentVariableA', 'CreateDirectoryExA', 'K32GetModuleBaseNameW', 'BaseQueryModuleData', 'FreeUserPhysicalPages', 'uaw_wcsicmp', 'GetCurrentConsoleFont', 'BaseUpdateAppcompatCache', 'IsValidCalDateTime', 'TerminateThread', 'GetThreadPriorityBoost', 'WerUnregisterFileWorker', 'TermsrvRestoreKey', 'GetPackageId', 'RegGetKeySecurity', 'WaitForThreadpoolTimerCallbacks', 'GetCalendarDateFormat', 'SetDynamicTimeZoneInformation', 'GetProcessHeap', 'NeedCurrentDirectoryForExePathA', 'SetCriticalSectionSpinCount', 'GetFullPathNameTransactedW', 'GetBinaryTypeW', 'RemoveDirectoryW', 'FindFirstFileExA', 'GetFullPathNameTransactedA', 'NeedCurrentDirectoryForExePathW', 'QueryInformationJobObject', 'ReleaseSRWLockExclusive', 'CreateFileTransactedW', 'GetBinaryTypeA', 'GetProductInfo', 'FindFirstVolumeA', 'SetCommState', 'IsDebuggerPresent', 'ResizePseudoConsole', 'FindFirstVolumeW', 'WriteConsoleInputVDMA', 'FreeConsole', 'GetTapeStatus', 'WriteConsoleInputVDMW', 'RemoveDirectoryA', 'RegGetValueW', 'Wow64EnableWow64FsRedirection', 'TransactNamedPipe', 'RegGetValueA', 'VirtualAllocExNuma', 'timeGetTime', 'QueryActCtxSettingsW', 'GetLongPathNameW', 'WriteConsoleOutputCharacterW', 'DnsHostnameToComputerNameW', 'ResetWriteWatch', 'FindResourceW', 'WriteConsoleOutputCharacterA', 'GetLongPathNameA', 'Sleep', 'IsBadCodePtr', 'FindResourceA', 'VirtualAlloc', 'DnsHostnameToComputerNameA', 'IdnToUnicode'])
def getHash(provided_hash):
    for apiname in exports:
        hash = 0
        for c in apiname:
            hash = hash << 7 & 0xffffff00 | ( (0xFF&(hash << 7)) | (0xFF&(hash >> 0x19)) ^ ord(c))
            if(provided_hash==pack('<L', hash)):
                return apiname
    return ""

fn = getFunctionAt(currentAddress)
i = getInstructionAt(currentAddress)
while getFunctionContaining(i.getAddress()) == fn:
    nem = i.getMnemonicString()
    if nem == "CALL":
        target_address = i.getOpObjects(0)
        if target_address[0].toString()=='EBP':
            current_hash = bytes(pack('<L', getInt(currentAddress.add(int(target_address[1].toString(),16)))))
            current_function_from_hash = getHash(current_hash)
            setEOLComment(i.getAddress(), current_function_from_hash)
            print(i.getAddress().toString() + " " + nem + "[EBP + "+target_address[1].toString()+ "]" + " -> " + current_function_from_hash)
    i = i.getNext()
